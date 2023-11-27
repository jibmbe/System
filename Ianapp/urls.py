

from django.urls import path
from .views import dashboard, upload_avatar
from .views import about
from .views import signup
from .views import login
from .views import location_request
from .views import clear_avatar
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView
from . import views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
    path('signup/', signup, name='signup'),
     path('about/', about, name='about'),
    path('login/', login, name='login'),
     path('location_request/', location_request, name='location_request'),
     path('clear_avatar/', clear_avatar, name='clear_avatar'),
path('logout/', LogoutView.as_view(), name='logout'),
path('login/', LoginView.as_view(template_name='login.html'), name='login'),
path('login/', CustomLoginView.as_view(), name='login'),
path('contact/', views.contact, name='contact'),
    # Add other URLs as needed
]
