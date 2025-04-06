from django.urls import path
from . import views

urlpatterns = [
    path("", views.shopping_list, name='shopping_list'),
    path('add/', views.add_item, name='add_item'),
]