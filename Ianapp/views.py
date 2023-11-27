

# Ianapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, LocationRequestForm
from .models import UserProfile
from .models import Place,Event
from math import radians, sin, cos, sqrt, atan2
from .forms import AvatarForm, LocationForm, BioForm
from Ianapp.forms import BioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm, BioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView
from .forms import ContactForm



# views.py

# views.py

def location_request(request):
    if request.method == 'POST':
        location_form = LocationRequestForm(request.POST)
        if location_form.is_valid():
            latitude = location_form.cleaned_data['latitude']
            longitude = location_form.cleaned_data['longitude']

            # Get nearby data, including live events
            nearby_data = {
                'events': get_live_events(latitude, longitude),
                'other_data': get_nearby_data(latitude, longitude),
            }

            return render(request, 'location_request.html', {'location_form': location_form, 'nearby_data': nearby_data})
    else:
        location_form = LocationRequestForm()

    return render(request, 'location_request.html', {'location_form': location_form})


def get_live_events(latitude, longitude):
    # Your logic to fetch live events based on location
    # This can involve querying a database, calling an API, etc.
    live_events = [...]  # Replace with your actual logic
    return live_events

def get_nearby_data(requested_lat, requested_lon):
    # Your logic here to fetch nearby places and live events from the database
    # Example:
    places = Place.objects.all()
    events = Event.objects.all()

    nearby_data = {
        'nearby_places': [],
        'events': [],
    }

    for place in places:
        distance = haversine(requested_lat, requested_lon, place.latitude, place.longitude)
        if distance < 5:  # Adjust the distance threshold as needed
            nearby_data['nearby_places'].append(place)

    for event in events:
        # Adjust the logic to determine if an event is nearby
        distance = haversine(requested_lat, requested_lon, event.latitude, event.longitude)
        if distance < 5:  # Adjust the distance threshold as needed
            nearby_data['events'].append(event)

    return nearby_data


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            
            # Log in the user
            login(request, user)
            
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid login credentials.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f"Welcome, {self.request.user}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid login credentials.")
        return super().form_invalid(form)


@login_required(login_url='login')

def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    avatar_form = AvatarForm()
    location_form = LocationForm()

    context = {
        'user_profile': user_profile,
        'avatar_form': avatar_form,
        'location_form': location_form,
        # Add any other context variables needed for your dashboard
    }

    return render(request, 'dashboard.html', context)
def about(request):
    # Placeholder logic for the about view
    context = {
        'message': 'Welcome to the About page!',
    }
    return render(request, 'about.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import AvatarForm  # Import your actual form

@login_required(login_url='login')

def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    avatar_form = AvatarForm()
    location_form = LocationForm()
    bio_form = BioForm()

    context = {
        'user_profile': user_profile,
        'avatar_form': avatar_form,
        'location_form': location_form,
        'bio_form': bio_form,
        # Add any other context variables needed for your dashboard
    }

    return render(request, 'dashboard.html', context)



@login_required
def upload_avatar(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        avatar_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if avatar_form.is_valid():
            avatar_form.save()
            return redirect('dashboard')

    avatar_form = UserProfileForm(instance=user_profile)
    return render(request, 'upload_avatar.html', {'avatar_form': avatar_form})

def clear_avatar(request):
    # Your logic to clear the avatar
    return render(request, 'clear_avatar_template.html')



def contact(request):
    submission_status = None
    submission_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # ...

            submission_status = 'success'
            submission_message = 'Your message was sent successfully!'
        else:
            submission_status = 'error'
            submission_message = 'Please correct the errors in the form.'

    else:
        form = ContactForm()

    return render(request, 'Ianapp/contact.html', {'form': form, 'submission_status': submission_status, 'submission_message': submission_message})


