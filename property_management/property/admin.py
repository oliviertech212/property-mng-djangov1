from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
from .models import Property 

admin.site.register(Property)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Customize admin panel for User model."""
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_superuser", "is_active")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)