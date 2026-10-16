# Faili eesmärk: kirjeldada sisestusvorme ja kontrollida andmeid enne salvestamist.

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Subject, Task

COLORS = [("#8b82f6", "Lilla"), ("#4a9b82", "Roheline"), ("#d49a4c", "Kollane"), ("#d7808f", "Roosa"), ("#5d9ac9", "Sinine")]

# Kasuta Django autentimist ning määra väljade eestikeelsed sildid ja brauseri täitmisvihjed.
# Pärimine: AuthenticationForm kontrollib kasutajanime ja parooli; siin kohandame välju.
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Kasutajanimi", widget=forms.TextInput(attrs={"autofocus": True, "autocomplete": "username"}))
    password = forms.CharField(label="Parool", widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))

# UserCreationForm kontrollib paroolide sobivust ja salvestab parooli räsi.
# Django baasklass hoolitseb konto loomise ja parooli turvalise salvestamise eest.
class RegisterForm(UserCreationForm):
    # model valib andmemudeli; fields määrab, milliseid selle välju kasutaja muuta saab.
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

# ModelForm seob vormiväljad Subject-mudeliga; omanikku brauserist ei küsita.
class SubjectForm(forms.ModelForm):
    color = forms.ChoiceField(label="Värv", choices=COLORS)
    # model valib andmemudeli; fields määrab, milliseid selle välju kasutaja muuta saab.
    class Meta:
        model = Subject
        fields = ["name", "color"]

    # Konstruktor käivitub vormi loomisel. owner on sisselogitud kasutaja.
    # *args ja **kwargs edastavad ülejäänud argumendid, näiteks POST-andmed ja instance.
    def __init__(self, *args, owner, **kwargs):
        # super kutsub baasklassi konstruktori, mis valmistab ette Django vormiväljad.
        super().__init__(*args, **kwargs)
        self.owner = owner
        # Omanik tuleb sisselogitud sessioonist, mitte kasutaja saadetud vormiandmetest.
        self.instance.owner = owner

    # Eemalda servadest tühikud ja anna korduva nime korral arusaadav vormiviga.
    def clean_name(self):
        # cleaned_data sisaldab juba esmase kontrolli läbinud väärtusi; strip eemaldab servatühikud.
        name = self.cleaned_data["name"].strip()
        # Muutmisel jäta sama kirje kontrollist välja, et selle nimi iseendaga ei kattuks.
        if Subject.objects.filter(owner=self.owner, name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Selle nimega õppeaine on sul juba olemas.")
        # Tagasta puhastatud nimi, mida vorm kasutab salvestamisel.
        return name

# Ülesande vorm lubab sisestada ainult Meta.fields loendis nimetatud välju.
class TaskForm(forms.ModelForm):
    # datetime-local saadab kuupäeva ja kellaaja ilma vööndita; Django kasutab seadistatud ajavööndit.
    due_at = forms.DateTimeField(label="Tähtaeg", input_formats=["%Y-%m-%dT%H:%M"], widget=forms.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}))
    # model valib andmemudeli; fields määrab, milliseid selle välju kasutaja muuta saab.
    class Meta:
        model = Task
        fields = ["title", "subject", "due_at", "description"]
        widgets = {"description": forms.Textarea(attrs={"rows": 4, "placeholder": "Mida selle ülesande puhul meeles pidada?"}), "title": forms.TextInput(attrs={"placeholder": "Näiteks: lõpeta arenduskavand"})}

    # Konstruktor käivitub vormi loomisel. owner on sisselogitud kasutaja.
    # *args ja **kwargs edastavad ülejäänud argumendid, näiteks POST-andmed ja instance.
    def __init__(self, *args, owner, **kwargs):
        # super kutsub baasklassi konstruktori, mis valmistab ette Django vormiväljad.
        super().__init__(*args, **kwargs)
        # Piira nii valikumenüü kui ka valideerimine omaniku ainetega: võõrast ID-d ei saa salvestada.
        self.fields["subject"].queryset = Subject.objects.filter(owner=owner)
        self.fields["subject"].empty_label = "Vali õppeaine"
