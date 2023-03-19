from django.contrib import admin
from .models import GameScore

# Register your models here.


@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    model = GameScore
    list_display = [
        'user', 'game', 'score', 'max_number', 'operation', 'created'
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created',)
        return ()
