from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    review = models.TextField(max_length=255)
    featured = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review + ' by (' + str(self.user) + ')'
