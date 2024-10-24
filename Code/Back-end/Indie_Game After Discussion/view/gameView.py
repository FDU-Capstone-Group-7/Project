from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from Indie_Game.forms import GameForm
from ..model.game import Game

#homepage
def homepage(request):
    return render(request, 'game/index.html')


def add_show(request):
    if request.method =='POST':
        fm=GameForm(request.POST)
        if fm.is_valid():
            
            tt=fm.cleaned_data['title']
            description=fm.cleaned_data['description']
            date=fm.cleaned_data['releaseDate']
            url =fm.cleaned_data['homepageURL']
            image =fm.cleaned_data['image']
            reg=Game(title=tt,description=description,releaseDate=date,homepageURL=url, image=image)
            reg.save()

            # YOU can use this way also but in this you can't select particular data
            #fm.save()
            fm=GameForm()
    else:
            fm=GameForm()

    game_list=Game.objects.all()
    return render(request,'game/addandshow.html',{'form':fm , 'games':game_list})
#This function will update and add
def update_data(request,id):
    if request.method=='POST':
        pi=Game.objects.get(pk=id)
        fm=GameForm(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Game.objects.get(pk=id)
        fm=GameForm(instance=pi)
    return render(request,'game/addandshow.html',{'form':fm})
# This fun will delete the data
def delete_data(request,id):
    if request.method=='POST':
        pi = Game.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/create-new/')
