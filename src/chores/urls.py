from django.urls import path
from . import views

urlpatterns = [
    path('', views.chore_list, name='chore_list'),
    path('new/', views.chore_create, name='chore_create'),
]