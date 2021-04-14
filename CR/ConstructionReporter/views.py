from django.shortcuts import render
# from .models import Defect, Respondent, MediaFile, Location, LocationType
from .forms import LocationTypeForm, LocationForm, DefectStatusForm, DefectForm
from .models import LocationType, Location, DefectStatus, Defect
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

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


def create_a_defect_status(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        defect_statuses = load_defect_statuses()
        context = {
            'defect_statuses': defect_statuses,

        }
        return render(request, 'ConstructionReporter/create_a_defect_status.html', context)


def create_a_defect_status_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = DefectStatusForm(request.POST)
        if form.is_valid():
            save_new_object(form)
            messages.info(request, "Location status successfully created")
            return redirect('/', {'form': form})
        else:
            messages.info(request, "Such location status already exists")
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
        groups = load_groups()
        print(locations)
        context = {
            'locations': locations,
            'location_types': location_types,
            'groups': groups
        }
        return render(request, 'ConstructionReporter/create_a_location.html', context)


def create_a_location_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = LocationForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.field1 = request.user
            # obj.save()
            form.save()
            messages.info(request, "Location successfully created")
            return redirect('/', {'form': form})
        else:
            print("form:")
            print(form)
            print("form ends")
            messages.info(request, "Such location already exists")
            return render(request, 'ConstructionReporter/index.html')


def create_a_defect(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        locations = load_locations()
        defects = load_defects()
        groups = load_groups()
        defect_statuses = load_defect_statuses()
        print(locations)
        context = {
            'locations': locations,
            'defects': defects,
            'groups': groups,
            'defect_statuses': defect_statuses,
        }
        return render(request, 'ConstructionReporter/create_a_defect.html', context)


def create_a_defect_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = DefectForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.field1 = datetime.now()
            # # obj.field2 = request.user
            # obj.save()
            form.save()
            messages.info(request, "Defect successfully created")
            return redirect('/', {'form': form})
        else:
            print("form:")
            print(form)
            print("form ends")
            messages.info(request, "Such location already exists")
            return render(request, 'ConstructionReporter/index.html')


def load_locations():
    locations = Location.objects.all()
    return locations


def load_groups():
    groups = Group.objects.all()
    return groups


def load_defects():
    defects = Defect.objects.all()
    return defects


def load_defect_statuses():
    defect_statuses = DefectStatus.objects.all()
    return defect_statuses
