from django import forms

from movie.models import Movie, Genre, Country


class MovieForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    countries = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Movie
        fields = "__all__"
