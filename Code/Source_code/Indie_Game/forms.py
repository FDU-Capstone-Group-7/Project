from django.core import validators
from django import forms
from .model.game import Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .model.userprofile import UserProfile
from .model.Discussion import Discussion, Comment_temp
from .model.update import Update
from django.core.exceptions import ValidationError

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'publisher', 'genre', 'stage', 'cover_image', 'video_link', 'description','short_intro']
        widgets = {
            'short_intro': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

    def clean_short_intro(self):
        data = self.cleaned_data['short_intro']
        word_count = len(data.split())
        if word_count > 30:
            raise forms.ValidationError(f"The short introduction cannot exceed 30 words. You provided {word_count} words.")
        return data


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     avatar = forms.ImageField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']


    def clean_username(self):
        username = self.cleaned_data.get('username')

 
        if User.objects.filter(username=username).exists():
            raise ValidationError("The username is already taken. Please choose a different username.")
        
        return username

    def save(self, commit=True):
  
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']


        if 'avatar' in self.cleaned_data:
            user.avatar = self.cleaned_data['avatar']

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

class EmailForm(forms.Form):
    email = forms.EmailField(label="Your Email", required=True)