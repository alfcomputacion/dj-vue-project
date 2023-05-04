import json
import html
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


def email_contact_us(request):
    data = json.loads(request.body)

    print(data)

    user = str(request.user)
    email = html.escape(data["email"])
    subject = html.escape(data["subject"])
    print(subject)
    message = html.escape(data["message"])
    if len(message) > 499:
        message = message[0:500]

    content = f'''
            <p>Dear Manager, </p>
            <p>User: {user}</p>
            <p>{message}</p>
            <p>from: {email}</p>'''

    send_email(to='alfcomputacion@gmail.com',
               subject=subject, content=content)

    response = {
        "success": True
    }
    return JsonResponse(response)
