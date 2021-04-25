from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'defects', views.DefectViewSet)

app_name = 'ConstructionReporter'
urlpatterns = [
    # path('', views.index, name='index'),
    path('location_type_creation', views.create_a_location_type, name='create_a_location_type'),
    path('location_type_creation/new', views.create_a_location_type_new, name='create_a_location_type_new'),
    path('defect_status_creation', views.create_a_defect_status, name='create_a_defect_status'),
    path('defect_status_creation/new', views.create_a_defect_status_new, name='create_a_defect_status_new'),
    path('location_creation', views.create_a_location, name='create_a_location'),
    path('location_creation/new', views.create_a_location_new, name='create_a_location_new'),
    path('defect_creation', views.create_a_defect, name='create_a_defect'),
    path('defect_creation/new', views.create_a_defect_new, name='create_a_defect_new'),
    path('index', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]