import json
import html
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import UpdateView, ListView
from .models import Review

from .forms import ReviewForm

from .models import Review

# Create your views here.


def send_review(request):
    data = json.loads(request.body)

    user = request.user
    tmp_review = data["message"]
    review = html.escape(tmp_review)
    if len(review) > 254:
        review = review[0:255]
    featured = False

    newReview = Review(user=user, review=review, featured=featured)
    newReview.save()

    response = {
        "success": True
    }

    return JsonResponse(response)


class ReviewUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Update Successful'
    success_url = reverse_lazy('users:users-list')


class ReviewListView(ListView):
    model = Review
    paginate_by = 5
