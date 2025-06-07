from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
       # Form-based URLs
       path('register/', views.register, name='register'),
       path('login/', views.login_view, name='login'),
       path('logout/', views.logout_view, name='logout'),
       path('', views.home, name='home'),
       path('check-login/', views.check_login, name='check_login'),
       # API URLs
       path('api/register/', views.RegisterAPI.as_view(), name='api_register'),
       path('api/login/', views.LoginAPI.as_view(), name='api_login'),
       path('api/logout/', views.LogoutAPI.as_view(), name='api_logout'),
       path('api/user/', views.UserAPI.as_view(), name='api_user'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]