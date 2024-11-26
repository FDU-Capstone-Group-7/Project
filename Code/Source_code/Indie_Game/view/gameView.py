from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from Indie_Game.forms import GameForm
from ..model.game import Game
from ..model.picture import Picture
from django.contrib.auth.decorators import login_required
from ..decorators import is_owner
from ..model.homepage import Homepage
from django.urls import reverse
from django.db.models import Q


def homepage(request):
    query = request.GET.get('q', '')
    game_list=Game.objects.all().order_by('-game_rating', 'title')


    if query: 
        game_list = game_list.filter(
            Q(title__icontains=query) |  # 
            Q(genre__icontains=query) |  # 
            Q(publisher__icontains=query)  
        ).distinct()

    return render(request, 'game/index.html',{'games': game_list,'query': query})




@login_required
def add_show(request):
    if request.method =='POST':
        fm=GameForm(request.POST,request.FILES)
        if fm.is_valid():
            
            title = fm.cleaned_data['title']
            publisher = fm.cleaned_data['publisher']
            stage = fm.cleaned_data['stage']
            cover_image = fm.cleaned_data['cover_image']
            video_link = fm.cleaned_data['video_link']
            pictures = request.FILES.getlist('pictures')
            description = fm.cleaned_data['description']
            short_intro = fm.cleaned_data['short_intro']
            user_profile = request.user.userprofile
            selected_genres = request.POST.getlist('genre')
            genre = ', '.join(selected_genres)

           
            reg = Game(
                title=title,
                publisher=publisher,
                genre=genre,
                stage=stage,
                cover_image=cover_image,
                video_link=video_link,
                description=description,
                short_intro=short_intro,
                owner=user_profile
            )

            reg.save()

            for picture in pictures:
                Picture.objects.create(game=reg, image=picture)
            
            
            
            homepage = Homepage(
                user=user_profile,
                game=reg
            )
            
            homepage.save()


            return HttpResponseRedirect(f'/game/{homepage.slug}/')
    else:
            fm=GameForm()

    game_list=Game.objects.all()
    return render(request,'game/addandshow.html',{'form':fm , 'games':game_list})

#This function will update and add
@login_required
@is_owner
def update_data(request,id):
    if request.method=='POST':
        pi=Game.objects.get(pk=id)
        fm=GameForm(request.POST ,request.FILES, instance=pi)
        new_pictures = request.FILES.getlist('pictures')
        if fm.is_valid():
            fm.save()

            Picture.objects.filter(game=pi).delete()
            for picture in new_pictures:
                Picture.objects.create(game=pi, image=picture)
            
        return HttpResponseRedirect(reverse('user_library'))
    
    else:
        pi=Game.objects.get(pk=id)
        fm=GameForm(instance=pi)
    return render(request,'game/updateGame.html',{'form':fm})

# This fun will delete the data
@login_required
@is_owner
def delete_data(request,id):
    if request.method=='POST':
        pi = Game.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('user_library'))
