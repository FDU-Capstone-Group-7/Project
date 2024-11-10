from django.contrib import admin
from django.urls import path
from Indie_Game.view import gameView
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from Indie_Game.view.userRegistration import signup_developer, signup_player
from django.contrib.auth import views as auth_views
from Indie_Game.view.gameHomepage import game_homepage
from Indie_Game.view.userLibrary import user_library
from django.urls import path
from Indie_Game.view import discussionView
from Indie_Game.view import updateView



urlpatterns = [
    path('admin/', admin.site.urls),
    #authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/developer/', signup_developer, name='signup_developer'), 
    path('accounts/signup/player/', signup_player, name='signup_player'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', gameView.homepage, name='home'),

    #Game Functions
    path('create-new/', gameView.add_show, name='create-new'),
    path('create-new/', gameView.add_show, name='manage-games'),
    path('update-game/<int:id>/', gameView.update_data, name='update_data'),
    path('delete-game/<int:id>/', gameView.delete_data, name='delete_data'),
    path('<int:id>/',gameView.update_data, name="updatedata"),
    path('game/<slug:slug>/', game_homepage, name='game_homepage'),
    path('library/', user_library, name='user_library'),

   #discussion url
    path('games/<int:game_id>/discussions/', discussionView.game_discussions, name='game_discussions'),
    path('games/<int:game_id>/discussions/create/', discussionView.create_discussion, name='create_discussion'),
    path('discussions/<int:discussion_id>/', discussionView.discussion_detail, name='discussion_detail'),
    path('discussions/<int:discussion_id>/delete/', discussionView.delete_discussion, name='delete_discussion'),

    
   #update url

    path('game/<slug:slug>/updates/create/', updateView.add_show_update, name='update_create'),
    path('game/<slug:slug>/updates/<int:update_id>/edit/', updateView.update_update, name='update_edit'),
    path('game/<slug:slug>/updates/<int:update_id>/delete/', updateView.delete_update, name='update_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)