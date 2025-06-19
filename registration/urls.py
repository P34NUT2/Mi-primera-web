from django.urls import path
from .views import UserRegisterView, UserLoginView, ProfileUpdateView, ProfileDetailView, ProfileTaskView, PublicProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<slug:username>/', ProfileDetailView.as_view(), name='profile-view'),
    path('public/profile/<slug:username>/', PublicProfileView.as_view(), name='public-profile'),
    path('profile/edit/<slug:username>/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/list-task/<slug:username>/', ProfileTaskView.as_view(), name='profile-tasks'),
]
 