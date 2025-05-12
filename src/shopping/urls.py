from django.urls import path
from shopping.views import ShoppingListView, AddItemView

urlpatterns = [
    path("", ShoppingListView.as_view(), name='shopping_list'),
    path('add/', AddItemView.as_view(), name='add_item'),
]