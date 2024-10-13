from django.core import validators
from django import forms
from .model.game import Game
from .model.discussion import Discussion, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .model.userprofile import UserProfile

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


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']