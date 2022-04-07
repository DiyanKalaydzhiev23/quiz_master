from django.urls import path
from quiz_master.accounts.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name='register'),
    path('sign-in/', UserLoginView.as_view(), name='login'),
    path('sign-out/', UserLogoutView.as_view(), name='logout')
]
