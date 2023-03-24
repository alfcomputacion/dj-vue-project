import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView

from common.utils.email import send_email

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'


class ContactUsView(TemplateView):
    template_name = 'pages/contact-us.html'


class ReviewView(TemplateView):
    template_name = 'pages/review.html'


def send_review_email(request):
    data = json.loads(request.body)

    user = request.user
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    content = str(user) + "  " + message

    send_email(to='alfcomputacion@gmail.com', subject=subject, content=content)

    response = {
        "success": True
    }
    return JsonResponse(response)
