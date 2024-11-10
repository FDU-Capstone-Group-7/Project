from django.core import validators
from django import forms
from .model.game import Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .model.userprofile import UserProfile
from .model.Discussion import Discussion, Comment_temp
from .model.update import Update

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'publisher', 'genre', 'stage', 'cover_image', 'video_link', 'description']


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
        model = Comment_temp
        fields = ['content']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ['update_title','update_date', 'patch_notes', 'downloadable', 'video']