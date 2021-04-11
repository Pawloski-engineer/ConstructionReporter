from django.urls import path
from . import views

app_name = 'COnstructionReporter'
urlpatterns = [
    path('', views.index, name='index'),
]