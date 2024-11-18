from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms import CustomUserCreationForm
from ..model.userprofile import UserProfile

def signup_developer(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')
 
            UserProfile.objects.create(user=user, account_type='dev', avatar=avatar)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm() 
    return render(request, 'registration/signup_developer.html', {'form': form})

def signup_player(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')
            UserProfile.objects.create(user=user, account_type='player', avatar=avatar)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  
    return render(request, 'registration/signup_player.html', {'form': form})
