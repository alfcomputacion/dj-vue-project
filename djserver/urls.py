"""djserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games.views import record_score
from games.views import show_ledear_board, show_score, get_user
from pages.views import send_review_email

urlpatterns = [
    path('admin/', admin.site.urls),

    # User admin
    path('account/my-account/', include('users.urls')),
    path('account/', include('allauth.urls')),

    path('', include('pages.urls')),
    path('games/', include('games.urls')),

    path('record-score/', record_score, name='record-score'),
    path('send-review/', send_review_email, name='send-review'),

    path('api/show-scores/', show_score, name='show-score'),
    path('api/leader-board/', show_ledear_board, name='leader-board'),

    path('api/user/', get_user, name='get-user'),

]
