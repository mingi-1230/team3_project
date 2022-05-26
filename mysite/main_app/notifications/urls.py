
from django.urls import path, include
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('notifications', views.index, name='index'),
]
