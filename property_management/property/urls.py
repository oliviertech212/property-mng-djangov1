
from django.urls import path
from .views import (
    # admin_register,
    landlord_register,
    tenant_register,
    admin_dashboard,
    landlord_dashboard,
    tenant_dashboard,
    property_list,
)
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    # path('register/admin/', admin_register, name='admin_register'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('register/landlord/', landlord_register, name='landlord_register'),
    path('register/tenant/', tenant_register, name='tenant_register'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('landlord/dashboard/', landlord_dashboard, name='landlord_dashboard'),
    path('tenant/dashboard/', tenant_dashboard, name='tenant_dashboard'),
    path('properties/', property_list, name='property_list'),
]