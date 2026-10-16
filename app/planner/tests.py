"""Regressioonitestid. TestCase loob eraldatud testiandmebaasi ning client jäljendab HTTP-päringuid."""
from datetime import timedelta
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Subject, Task


class PlannerTests(TestCase):
    # Iga test saab kaks kasutajat: nii saab kontrollida ka võõraste andmete kaitset.
    def setUp(self):
        self.user = User.objects.create_user("õpilane", password="Test-Password-842!")
        self.other = User.objects.create_user("teine", password="Test-Password-927!")
        self.subject = Subject.objects.create(owner=self.user, name="Matemaatika")
        self.foreign_subject = Subject.objects.create(owner=self.other, name="Teise aine")
        self.task = Task.objects.create(subject=self.subject, title="Minu töö", due_at=timezone.now() + timedelta(days=2))
        self.foreign_task = Task.objects.create(subject=self.foreign_subject, title="Võõras töö", due_at=timezone.now() + timedelta(days=1))
        self.client.force_login(self.user)

    # Tagasta korrektne vormisisend; changes võimaldab testida üksikut muudatust.
    def payload(self, **changes):
        data = {"title": "Uus ülesanne", "subject": self.subject.pk, "due_at": "2027-05-10T14:30", "description": "Märkmed"}
        data.update(changes)
        return data

    def test_full_workflow_create_edit_complete_restore_delete(self):
        response = self.client.post(reverse("task_create"), self.payload())
        self.assertRedirects(response, reverse("dashboard"))
        task = Task.objects.get(title="Uus ülesanne")
        self.assertEqual(task.description, "Märkmed")
        self.client.post(reverse("task_edit", args=[task.pk]), self.payload(title="Muudetud töö"))
        task.refresh_from_db()
        self.assertEqual(task.title, "Muudetud töö")
        self.client.post(reverse("task_toggle", args=[task.pk]), {"completed": "1"})
        self.client.post(reverse("task_toggle", args=[task.pk]), {"completed": "1"})
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.assertNotContains(self.client.get(reverse("dashboard")), "Muudetud töö")
        self.assertContains(self.client.get(reverse("dashboard"), {"status": "done"}), "Muudetud töö")
        self.client.post(reverse("task_toggle", args=[task.pk]), {"completed": "0"})
        task.refresh_from_db()
        self.assertFalse(task.completed)
        response = self.client.get(reverse("task_delete", args=[task.pk]))
        self.assertContains(response, "Kustuta ülesanne?")
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
        self.client.post(reverse("task_delete", args=[task.pk]))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_other_users_data_is_hidden_in_all_views(self):
        for path in [reverse("dashboard"), reverse("dashboard") + "?status=all", reverse("calendar"), reverse("subjects")]:
            self.assertNotContains(self.client.get(path), "Võõras töö")
            self.assertNotContains(self.client.get(path), "Teise aine")
        response = self.client.get(reverse("dashboard"), {"subject": self.foreign_subject.pk, "status": "all"})
        self.assertEqual(list(response.context["page"]), [])

    def test_foreign_task_endpoints_return_404_and_preserve_data(self):
        for endpoint in ["task_edit", "task_delete"]:
            self.assertEqual(self.client.get(reverse(endpoint, args=[self.foreign_task.pk])).status_code, 404)
            self.assertEqual(self.client.post(reverse(endpoint, args=[self.foreign_task.pk]), self.payload()).status_code, 404)
        response = self.client.post(reverse("task_toggle", args=[self.foreign_task.pk]), {"completed": "1"})
        self.assertEqual(response.status_code, 404)
        self.foreign_task.refresh_from_db()
        self.assertFalse(self.foreign_task.completed)
        self.assertEqual(self.foreign_task.title, "Võõras töö")

    def test_forged_subject_and_empty_title_are_rejected(self):
        for changes in [{"subject": self.foreign_subject.pk}, {"title": "  "}, {"due_at": "vale"}]:
            response = self.client.post(reverse("task_create"), self.payload(**changes))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.context["form"].errors)
        self.assertEqual(Task.objects.count(), 2)

    def test_duplicate_subject_only_rejected_for_same_owner(self):
        data = {"name": "Matemaatika", "color": "#8b82f6"}
        response = self.client.post(reverse("subjects"), data)
        self.assertTrue(response.context["form"].errors)
        self.client.force_login(self.other)
        self.assertRedirects(self.client.post(reverse("subjects"), data), reverse("subjects"))

    def test_order_overdue_and_combined_filters(self):
        overdue = Task.objects.create(subject=self.subject, title="Vana töö", due_at=timezone.now() - timedelta(days=1))
        done = Task.objects.create(subject=self.subject, title="Lõpetatud", due_at=timezone.now(), completed=True)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual([t.pk for t in response.context["page"]], [overdue.pk, self.task.pk])
        self.assertContains(response, "Hilinenud")
        response = self.client.get(reverse("dashboard"), {"subject": self.subject.pk, "status": "done", "q": "Lõpetatud"})
        self.assertEqual([t.pk for t in response.context["page"]], [done.pk])
        response = self.client.get(reverse("dashboard"), {"q": "puudub"})
        self.assertContains(response, "Ühtegi vastet ei leitud")

    def test_today_filter_and_invalid_filters(self):
        task = Task.objects.create(subject=self.subject, title="Täna", due_at=timezone.now())
        response = self.client.get(reverse("dashboard"), {"status": "today"})
        self.assertEqual([t.pk for t in response.context["page"]], [task.pk])
        self.assertEqual(self.client.get(reverse("dashboard"), {"subject": "abc", "status": "invalid", "page": "no"}).status_code, 200)

    def test_calendar_boundaries_and_week_switch(self):
        response = self.client.get(reverse("calendar"), {"week": "2027-05-10"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["days"]), 7)
        self.assertEqual(response.context["monday"].isoformat(), "2027-05-10")
        self.client.post(reverse("task_create"), self.payload())
        response = self.client.get(reverse("calendar"), {"week": "2027-05-10"})
        self.assertEqual(len(response.context["days"][0]["tasks"]), 1)
        self.assertNotContains(self.client.get(reverse("calendar"), {"week": "2027-05-17"}), "Uus ülesanne")
        self.assertEqual(self.client.get(reverse("calendar"), {"week": "vigane"}).status_code, 200)

    def test_toggle_requires_post_and_valid_state(self):
        self.assertEqual(self.client.get(reverse("task_toggle", args=[self.task.pk])).status_code, 405)
        self.assertEqual(self.client.post(reverse("task_toggle", args=[self.task.pk]), {"completed": "abc"}).status_code, 400)

    def test_csrf_required_for_changes(self):
        secure_client = Client(enforce_csrf_checks=True)
        secure_client.force_login(self.user)
        response = secure_client.post(reverse("task_toggle", args=[self.task.pk]), {"completed": "1"})
        self.assertEqual(response.status_code, 403)

    def test_registration_login_logout(self):
        self.client.logout()
        response = self.client.post(reverse("register"), {"username": "uusopilane", "password1": "Kool-Proov-249!", "password2": "Kool-Proov-249!"})
        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 200)
        self.client.post(reverse("logout"))
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 302)
        response = self.client.post(reverse("login"), {"username": "uusopilane", "password": "wrong"})
        self.assertContains(response, "Logi sisse")
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertRedirects(self.client.post(reverse("login"), {"username": "uusopilane", "password": "Kool-Proov-249!"}), reverse("dashboard"))

    def test_subject_required_before_first_task(self):
        newcomer = User.objects.create_user("uus", password="Test-8935!")
        self.client.force_login(newcomer)
        self.assertRedirects(self.client.get(reverse("task_create")), reverse("subjects"))

    def test_pagination_and_xss_escaping(self):
        Task.objects.bulk_create([Task(subject=self.subject, title=f"Töö {i}", due_at=timezone.now()) for i in range(30)])
        response = self.client.get(reverse("dashboard"), {"status": "all", "subject": self.subject.pk})
        self.assertEqual(len(response.context["page"]), 25)
        self.assertContains(response, "Järgmine")
        Task.objects.create(subject=self.subject, title='<script>alert("x")</script>', due_at=timezone.now()-timedelta(days=1))
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "&lt;script&gt;")
        self.assertNotContains(response, '<script>alert("x")</script>')
