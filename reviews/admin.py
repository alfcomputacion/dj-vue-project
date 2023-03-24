from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review

    list_display = [
        'user', 'review', 'featured', 'created'
    ]

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ('created',)
        return ()
