from datetime import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CustomUserForm(UserChangeForm):
    password = None

    class Meta:
        BIRTH_DATE_CHOICES = range(1915, datetime.now().year)
        model = get_user_model()
        fields = ('avatar', 'email', 'username',
                  'first_name', 'last_name', 'dob', 'is_staff', 'is_admin')
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years=BIRTH_DATE_CHOICES
            )
        }
        help_texts = {
            'is_admin': 'Turns user into admin.'
        }
