from django.urls import path
from .views import ReviewUpdateView, ReviewListView

app_name = 'reviews'
urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/update/',
         ReviewUpdateView.as_view(), name='review-update'),
]
