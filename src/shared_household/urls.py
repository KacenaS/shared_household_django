
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import welcome, RegisterView, guest_login

urlpatterns = [
    path('', welcome, name='welcome'),
    path("admin/", admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('shopping/', include('shopping.urls')),
    path('chores/', include('chores.urls')),
    path('finances/', include('finances.urls')),
    # LOgin
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('guest-login/', guest_login, name='guest_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
