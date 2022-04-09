from django.urls import path
from quiz_master.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileView

urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name='register'),
    path('sign-in/', UserLoginView.as_view(), name='login'),
    path('sign-out/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]
