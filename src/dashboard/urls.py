from django.urls import path
from . import views
from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
]