from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from .forms import CustomUserForm
from .models import CustomUser
from django.urls import reverse_lazy
# Create your views here.


class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserForm
    template_name = 'account/my_account.html'

    success_message = 'Update Successful.'
    success_url = reverse_lazy('my-account')

    def get_object(self):
        return self.request.user


class UserAdminPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserForm
    template_name = 'users/customuser_form.html'

    success_message = 'Update Successful.'
    success_url = reverse_lazy('users:users-list')

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        return super().form_valid(form)


class CustomUserList(LoginRequiredMixin, ListView):
    model = CustomUser
    paginate_by = 10

    def get_queryset(self):
        qs = CustomUser.objects.all()

        if 'q' in self.request.GET:
            q = self.request.GET.get('q')
            qs = qs.filter(username__icontains=q)
        return qs.order_by('username')


class CustomUserDetail(DetailView):
    model = CustomUser


class CustomUserDelete(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users:users-list')
