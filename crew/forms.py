from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Director, Actor
from movie.models import Country


class DirectorCreationForm(UserCreationForm):
    birthday = forms.DateField(required=False)
    photo = forms.ImageField(required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False)

    class Meta(UserCreationForm.Meta):
        model = Director
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "birthday",
            "photo",
            "country",
        )
