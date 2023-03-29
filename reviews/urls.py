from django.urls import path
from .views import email_contact_us

urlpatterns = [
    path('', email_contact_us, name='email-contact-us')
]
