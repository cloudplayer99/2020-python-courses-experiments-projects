from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('5', views.champion, name='champion'),
]
