from django.urls import path
from . import views

app_name = 'markers'

urlpatterns = [
    path('', views.index, name='index'),
]