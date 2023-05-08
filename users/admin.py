from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('avatar', 'dob',)}),
        (None, {'fields': ('is_admin',)}),
    ) + UserAdmin.fieldsets

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'avatar', 'dob', 'is_staff', 'is_admin'),
        }),
    )
