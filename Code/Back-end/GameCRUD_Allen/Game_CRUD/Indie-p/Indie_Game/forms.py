from django.core import validators
from django import forms
from .model.game import Game

class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields = ['title','description', 'releaseDate', 'homepageURL', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Game Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter Description'}),
            'releaseDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'homepageURL': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Homepage URL'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }