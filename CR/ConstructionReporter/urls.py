from django.urls import path
from . import views

app_name = 'ConstructionReporter'
urlpatterns = [
    path('', views.index, name='index'),
    path('location_type_creation', views.create_a_location_type, name='create_a_location_type'),
    path('location_type_creation/new', views.create_a_location_type_new, name='create_a_location_type_new'),
    path('index', views.index, name='index'),

]