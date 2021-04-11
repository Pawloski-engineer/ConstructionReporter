from django.shortcuts import render
# from .models import Defect, Respondent, MediaFile, Location, LocationType, UserGroup
from .forms import LocationTypeForm, LocationForm
from .models import LocationType
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'ConstructionReporter/index.html')

def create_a_location_type(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'ConstructionReporter/create_a_location_type.html')

def create_a_location_type_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = LocationTypeForm(request.POST)
        if form.is_valid():
            save_new_location_type(form)
            messages.info(request, "Location type successfully created")
            return redirect('', {'form': form})
        else:
            print('inform_user_no_building_name')

def save_new_location_type(form):
    location_type = form.save(commit=False)
    location_type.save()