from django.urls import path
from quiz_master.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, profile_view, EditProfile, \
    DeleteUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', profile_view, name='profile'),
    path('edit-profile/<int:pk>', EditProfile.as_view(), name="edit profile"),
    path('delete-profile/<int:pk>', DeleteUserView.as_view(), name="delete profile"),
]
