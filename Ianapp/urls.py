

from django.urls import path
from .views import dashboard, upload_avatar
from .views import about
from .views import signup

from .views import location_request
from .views import clear_avatar



from . import views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
    path('signup/', signup, name='signup'),
     path('about/', about, name='about'),
    
     path('location_request/', location_request, name='location_request'),
     path('clear_avatar/', clear_avatar, name='clear_avatar'),



path('contact/', views.contact, name='contact'),
path('profile/', views.profile, name='profile'), 
    # Add other URLs as needed
]
