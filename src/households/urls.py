from django.urls import path
from .views import CreateHouseholdView, JoinHouseholdView, HouseholdListView

urlpatterns = [
    path('create/', CreateHouseholdView.as_view(), name='create_household'),
    path('join/', JoinHouseholdView.as_view(), name='join_household'),
    path('', HouseholdListView.as_view(), name='household_list'),
    #path('<int:pk>/', HouseholdDetailView.as_view(), name='household_detail'),
]