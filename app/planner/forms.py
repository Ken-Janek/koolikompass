from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Subject, Task

COLORS = [("#8b82f6", "Lilla"), ("#4a9b82", "Roheline"), ("#d49a4c", "Kollane"), ("#d7808f", "Roosa"), ("#5d9ac9", "Sinine")]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Kasutajanimi", widget=forms.TextInput(attrs={"autofocus": True, "autocomplete": "username"}))
    password = forms.CharField(label="Parool", widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class SubjectForm(forms.ModelForm):
    color = forms.ChoiceField(label="Värv", choices=COLORS)
    class Meta:
        model = Subject
        fields = ["name", "color"]

    def __init__(self, *args, owner, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner
        self.instance.owner = owner

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if Subject.objects.filter(owner=self.owner, name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Selle nimega õppeaine on sul juba olemas.")
        return name

class TaskForm(forms.ModelForm):
    due_at = forms.DateTimeField(label="Tähtaeg", input_formats=["%Y-%m-%dT%H:%M"], widget=forms.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}))
    class Meta:
        model = Task
        fields = ["title", "subject", "due_at", "description"]
        widgets = {"description": forms.Textarea(attrs={"rows": 4, "placeholder": "Mida selle ülesande puhul meeles pidada?"}), "title": forms.TextInput(attrs={"placeholder": "Näiteks: lõpeta arenduskavand"})}

    def __init__(self, *args, owner, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subject"].queryset = Subject.objects.filter(owner=owner)
        self.fields["subject"].empty_label = "Vali õppeaine"
