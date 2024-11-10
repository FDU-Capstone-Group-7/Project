from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..model.update import Update
from ..model.updatePicture import UpdatePicture
from ..forms import UpdateForm  
from ..decorators import is_owner
from ..model.homepage import Homepage
from django.http import HttpResponseForbidden


@login_required
def add_show_update(request,slug):
    homepage = get_object_or_404(Homepage,slug=slug)

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():

            update_date = form.cleaned_data['update_date']
            patch_notes = form.cleaned_data['patch_notes']
            downloadable = form.cleaned_data['downloadable']
            video = form.cleaned_data['video']
            pictures = request.FILES.getlist('update_pictures')
            title = form.cleaned_data['update_title']



            new_update = Update(
                homepage=homepage,
                update_date=update_date,
                patch_notes=patch_notes,
                downloadable=downloadable,
                video=video,
                update_title=title,

            )
            new_update.save()

            for picture in pictures:
                UpdatePicture.objects.create(update=new_update, image=picture)


            return HttpResponseRedirect(f'/game/{homepage.slug}/')
    else:
        form = UpdateForm()

    updates = Update.objects.filter(homepage=homepage).order_by('-update_date')
    return render(request, 'game/addUpdate.html', {'form': form, 'updates': updates})


@login_required
@is_owner
def update_update(request,slug,update_id):
    homepage = get_object_or_404(Homepage,slug=slug)
    update_instance = get_object_or_404(Update, pk=update_id)


    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=update_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/game/{homepage.slug}/')
    else:
        form = UpdateForm(instance=update_instance)

    return render(request, 'game/editUpdate.html', {'form': form})


@login_required
@is_owner
def delete_update(request,slug, update_id):
    homepage = get_object_or_404(Homepage,slug=slug)
    update_instance = get_object_or_404(Update, pk=update_id)
    if request.method == 'POST':
        update_instance.delete()
        return HttpResponseRedirect(f'/game/{homepage.slug}/')

