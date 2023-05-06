from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError

# Create your models here.


def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 250 or h > 250:
        raise ValidationError(
            'Avatar must be no bigger than 250x250 pixels')


class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name='Date of Birth', null=True, blank=True
    )

    avatar = models.ImageField(upload_to='avatars/',
                               null=True, blank=True,
                               help_text='Image must be 250px by 250px',
                               validators=[validate_avatar])

    is_admin = models.BooleanField(verbose_name='Admin status',
                                   default=False)

    @property
    def num_reviews(self):
        return self.reviews.count()

    @property
    def user_reviews(self):
        return self.reviews.filter(user_id=self.id)
