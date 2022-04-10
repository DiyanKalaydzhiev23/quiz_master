from django.urls import reverse_lazy
from quiz_master.accounts.forms import CreateProfileForm
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from quiz_master.common.quizzes_get_view_and_context import get


UserModel = get_user_model()


def profile_view(request, pk=None, quiz_name=None):
    if request.method == 'GET':
        return get(request, pk, quiz_name, 'accounts/profile.html')
    else:
        return get(request, pk, request.POST.get('quiz_name'), 'accounts/profile.html')


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
