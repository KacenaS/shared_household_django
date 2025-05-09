from django.urls import path
from chores.views import ChoreListView, ChoreCreateView

urlpatterns = [
    path('', ChoreListView.as_view(), name='chore_list'),
    path('new/', ChoreCreateView.as_view(), name='chore_create'),
]