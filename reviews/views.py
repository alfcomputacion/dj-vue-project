import json
from django.http import JsonResponse

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
