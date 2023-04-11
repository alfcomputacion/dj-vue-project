from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from .forms import CustomUserForm
from .models import CustomUser
from django.urls import reverse_lazy
# Create your views here.


class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserForm
    template_name = 'account/my_account.html'

    success_url = reverse_lazy('users:my-account')

    def get_object(self):
        return self.request.user


class UserAdminPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserForm
    template_name = 'users/customuser_form.html'

    success_url = reverse_lazy('users:users-list')


class CustomUserList(LoginRequiredMixin, ListView):
    model = CustomUser


class CustomUserDetail(DetailView):
    model = CustomUser


class CustomUserDelete(DeleteView):
    model = CustomUser
    success_url = 'users:user-detail'
