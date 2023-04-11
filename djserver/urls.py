from django.contrib import admin
from django.urls import path, include
from games.views import record_score
from games.views import show_ledear_board, show_score, get_user

from pages.views import email_contact_us
from reviews.views import send_review

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/page/', include('users.urls')),
    path('admin/', admin.site.urls),

    # User admin
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),

    path('', include('pages.urls')),
    path('games/', include('games.urls')),

    path('record-score/', record_score, name='record-score'),
    path('send-review/', send_review, name='send-review'),
    path('send-email/', email_contact_us, name='email-contact-us'),

    path('api/show-scores/', show_score, name='show-score'),
    path('api/leader-board/', show_ledear_board, name='leader-board'),

    path('api/user/', get_user, name='get-user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
