import json
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import UpdateView, ListView
from .models import Review
from users.models import CustomUser
from django.contrib.auth import get_user_model
from .forms import ReviewForm

from .models import Review

# Create your views here.


def send_review(request):
    data = json.loads(request.body)

    user = request.user
    review = data["review"]
    featured = 1

    newReview = Review(user=user, review=review, featured=featured)
    newReview.save()

    response = {
        "success": True
    }

    return JsonResponse(response)


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('users:users-list')


class ReviewListView(ListView):
    model = Review
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        page = self.kwargs.get('page_obj')
        context['page'] = page
        print(context['page'])
        return context
