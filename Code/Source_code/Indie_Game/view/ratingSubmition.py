from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from ..model.update import Update
from ..model.rating import Rating
from ..model.homepage import Homepage


@login_required
def submit_rating(request, update_id, slug):
 
    update_instance = get_object_or_404(Update, pk=update_id)
    user = request.user.userprofile  
    homepage = get_object_or_404(Homepage, slug=slug)
    user_has_rated = False

  
    if Rating.objects.filter(user=user, update=update_instance).exists():
        user_has_rated = True

    if request.method == 'POST':
     
        if user_has_rated:
            messages.warning(request, 'You have already rated this update!')
            user_has_rated = True
            return redirect('game_homepage', slug=homepage.slug)

        score = float(request.POST['score'])  

    
        Rating.objects.create(user=user, update=update_instance, score=score, homepage=homepage)


        ratings = update_instance.ratings.all()  
        if ratings.exists():
            total_score = sum(rating.score for rating in ratings)  
            total_ratings = ratings.count() 
            average_rating = total_score / total_ratings  
            update_instance.average_rating = round(average_rating, 2)  
        else:
            update_instance.average_rating = 0.0  

   
        update_instance.save()

        user_has_rated = False
        

   
        return redirect('game_homepage', slug=homepage.slug)
    


