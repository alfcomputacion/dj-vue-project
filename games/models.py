from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.

class GameScore(models.Model):
    MATH = 'MATH'
    ANAGRAM = 'ANAGRAM'

    GAME_CHOICES = [
        (MATH, "Math Game"),
        (ANAGRAM, "Anagram Game")
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='scores')
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    max_number = models.IntegerField()
    operation = models.TextField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score)
