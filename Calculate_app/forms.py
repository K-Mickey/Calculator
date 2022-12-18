from django import forms


class MatchForm(forms.Form):
    problem = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите число'
    }))
