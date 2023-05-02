from django.urls import path

from .views import CustomUserList, CustomUserDetail, UserAdminPageView, CustomUserDelete
# MyAccountPageView,

app_name = 'users'
urlpatterns = [
    path('user-update/<int:pk>/', UserAdminPageView.as_view(), name='user-update'),
    path('user-detail/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('', CustomUserList.as_view(), name='users-list'),
    # path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('user/<int:pk>/delete/', CustomUserDelete.as_view(), name='user-delete'),
]
