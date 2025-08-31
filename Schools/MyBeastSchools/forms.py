from django import forms
from .models import Subject, Cabinet, Student


class SubjectForm(forms.Form):
    name = forms.CharField(
        label="Назва предмету",
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "bio", "cabinet", "subject"]

        first_name = forms.CharField(
        label="Ім'я",
        widget=forms.TimeInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        label="Додаткова інформація про користувача",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    cabinet = forms.ModelChoiceField(
        label="Виберіть кабінет",
        queryset=Cabinet.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"})
    )
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget = forms.SelectMultiple(attrs={"class": "form-select"}),
        label = "Виберіть предмети для навчання"
    )