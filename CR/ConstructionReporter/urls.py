from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'defects-detail', views.DefectViewSet)
router.register(r'defectstatus-detail', views.DefectStatusViewSet)
router.register(r'locationtype-detail', views.LocationTypeViewSet)
router.register(r'location-detail', views.LocationViewSet)
router.register(r'user-detail', views.UserViewSet)
router.register(r'group-detail', views.GroupViewSet)



app_name = 'ConstructionReporter'
urlpatterns = [
    path('', views.index, name='index'),
    path('location_type_creation', views.create_a_location_type, name='create_a_location_type'),
    path('location_type_creation/new', views.create_a_location_type_new, name='create_a_location_type_new'),
    path('defect_status_creation', views.create_a_defect_status, name='create_a_defect_status'),
    path('defect_status_creation/new', views.create_a_defect_status_new, name='create_a_defect_status_new'),
    path('location_creation', views.create_a_location, name='create_a_location'),
    path('location_creation/new', views.create_a_location_new, name='create_a_location_new'),
    path('defect_creation', views.create_a_defect, name='create_a_defect'),
    path('defect_creation/new', views.create_a_defect_new, name='create_a_defect_new'),
    path('defects', views.view_defects, name='view_defects'),
    path('index/', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sw.js', views.ServiceWorkerView.as_view(), name=views.ServiceWorkerView.name, ),

]