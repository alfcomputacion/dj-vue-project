from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from .forms import CustomUserForm

# Create your views here.


class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserForm
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
