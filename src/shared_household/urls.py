
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('shopping/', include('shopping.urls')),
    path('chores/', include('chores.urls')),
    path('finances/', include('finances.urls')),
    
]
