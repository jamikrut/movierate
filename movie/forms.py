from django import forms


class MovieForm(forms.Form):
    tmdb_id = forms.CharField(max_length=15, required=False, label='TMDB ID')
    title = forms.CharField(max_length=255, label='Tytuł')
    cast = forms.CharField(max_length=255, label='Obsada')
    homepage = forms.URLField(label='Strona WWW')
    director = forms.CharField(max_length=255, label='Reżyser')
    keywords = forms.CharField(max_length=255, label='Słowa kluczowe')
    overview = forms.CharField(max_length=1000, label='Opis', widget=forms.Textarea(attrs={'rows': 3}))
    runtime_min = forms.IntegerField(label='Czas trwania [minuty]')
    genres = forms.CharField(max_length=255, label='Gatunki [rozdzielone pipe]')
    production_companies = forms.CharField(max_length=1000, label='Producenci [rozdzielone pipe]')
    release_date = forms.DateField(label='Data produkcji', widget=forms.DateInput(attrs={"type": "date"}))

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'uk-input'