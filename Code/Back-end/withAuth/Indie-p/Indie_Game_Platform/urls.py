"""crud1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Indie_Game.view import gameView
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from Indie_Game.view.userRegistration import signup_developer, signup_player
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/developer/', signup_developer, name='signup_developer'), 
    path('accounts/signup/player/', signup_player, name='signup_player'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', gameView.homepage, name='home'),
    path('create-new/', gameView.add_show, name='create-new'),
    path('create-new/', gameView.add_show, name='manage-games'),
    path('update-game/',gameView.add_show, name="addandshow"),
    path('delete/<int:id>/',gameView.delete_data, name="deletedata"),
    path('<int:id>/',gameView.update_data, name="updatedata"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)