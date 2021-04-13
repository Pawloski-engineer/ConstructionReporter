from django.shortcuts import render
# from .models import Defect, Respondent, MediaFile, Location, LocationType, UserGroup
from .forms import LocationTypeForm, LocationForm
from .models import LocationType, Location
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'ConstructionReporter/index.html')


def create_a_location_type(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        location_types = load_location_types()
        context = {
            'location_types': location_types,

        }
        return render(request, 'ConstructionReporter/create_a_location_type.html', context)


def create_a_location_type_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = LocationTypeForm(request.POST)
        if form.is_valid():
            save_new_object(form)
            messages.info(request, "Location type successfully created")
            return redirect('/', {'form': form})
        else:
            messages.info(request, "Such location type already exists")
            return render(request, 'ConstructionReporter/index.html')


def save_new_object(form):
    new_object = form.save(commit=False)
    new_object.save()


def load_location_types():
    location_types = LocationType.objects.all()
    return location_types


def create_a_location(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        locations = load_locations()
        location_types = load_location_types()
        print(locations)
        context = {
            'locations': locations,
            'location_types': location_types
        }
        return render(request, 'ConstructionReporter/create_a_location.html', context)


def create_a_location_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = LocationForm(request.POST)
        if form.is_valid():
            save_new_object(form)
            messages.info(request, "Location successfully created")
            return redirect('/', {'form': form})
        else:
            messages.info(request, "Such location already exists")
            return render(request, 'ConstructionReporter/index.html')


def load_locations():
    locations = Location.objects.all()
    return locations
