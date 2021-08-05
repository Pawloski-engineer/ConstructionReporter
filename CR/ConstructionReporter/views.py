from django.shortcuts import render
# from .models import Defect, Respondent, MediaFile, Location, LocationType
from .forms import LocationTypeForm, LocationForm, DefectForm
from .models import LocationType, Location, Defect
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters, status
from .models import DefectSerializer, LocationTypeSerializer, LocationSerializer, UserSerializer, GroupSerializer

from django.views.generic import TemplateView
from django.templatetags.static import static
from django.urls import reverse

from django.core import serializers

version = '1.0.1'


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
        current_user = request.user
        context = {
            'locations': locations,
            'location_types': location_types,
            'groups': groups,
            'current_user': current_user
        }
        return render(request, 'ConstructionReporter/create_a_location.html', context)


def create_a_location_new(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form = LocationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            obj.location_admin.add(request.user.id)
            obj.save()
            messages.info(request, "Location successfully created")
            # TODO add refreshing location list in localstorage
            return redirect('/refresh_localstorage', {'form': form})
        else:
            # print("form:")
            # print(form)
            # print("form ends")
            # messages.info(request, "An error occurred")
            list_of_errors = form.errors
            print('__________________')
            print(type(list_of_errors))
            print('__________________')
            # messages.info(request, form.errors)
            try:
                messages.info(request, list_of_errors.pop('__all__'))
            except KeyError:
                messages.info(request, "Element does not exist")
            return render(request, 'ConstructionReporter/index.html')


def create_a_defect(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        locations = load_locations()
        defects = load_defects()
        groups = load_groups()
        defect_statuses = load_defect_statuses()
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
            obj = form.save(commit=False)
            # obj.save()
            obj.reporter = request.user
            obj.save()

            # form.save()
            messages.info(request, "Defect successfully created")
            return redirect('/', {'form': form})
        else:
            print("__________________form:__________________")
            print(form)
            print("__________________form ends__________________")
            messages.info(request, "An error occurred")
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


def view_defects(request):
    defects = load_defects()
    context = {'defects': defects}
    return render(request, 'ConstructionReporter/view_defects.html', context)


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all().order_by('creation_date')
    serializer_class = DefectSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        defect_data = request.data
        serializer = DefectSerializer(data=defect_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationTypeViewSet(viewsets.ModelViewSet):
    queryset = LocationType.objects.all().order_by('location_type_name')
    serializer_class = LocationTypeSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        location_type_data = request.data
        serializer = LocationTypeSerializer(data=location_type_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationViewSet(viewsets.ModelViewSet):
    search_fields = ['location_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Location.objects.all().order_by('location_type')
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        location_data = request.data
        serializer = LocationSerializer(data=location_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'

    def get_context_data(self, **kwargs):
        return {
            'version': version,
            'icon_url': static('images/hello-icon-512.png'),
            'manifest_url': static('manifest.json'),
            'style_url': static('css/style.css'),
            # 'home_url': reverse('ConstructionReporter:buildings_list'),
            'offline_url': reverse('ConstructionReporter:offline'),
        }


def offline(request):
    return render(request, 'ConstructionReporter/offline.html')


def refresh_localstorage(request):
    return render(request, 'ConstructionReporter/refresh_localstorage.html')
