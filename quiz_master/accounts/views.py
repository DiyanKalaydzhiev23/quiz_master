from django.urls import reverse_lazy
from quiz_master.accounts.forms import CreateProfileForm
from django.views import generic as views
from django.contrib.auth import views as auth_views


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/signin.html'
    success_url = reverse_lazy('quizzes')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    success_url = reverse_lazy('login')
