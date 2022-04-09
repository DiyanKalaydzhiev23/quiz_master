from django.urls import reverse_lazy
from quiz_master.accounts.forms import CreateProfileForm
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from quiz_master.accounts.models import Profile
from quiz_master.quiz_app.models import Quiz

UserModel = get_user_model()


class ProfileView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get(self, *args, **kwargs):
        is_owner = True if self.request.user.id == self.get_object().user_id else False

        context = {
            'profile': self.get_object(),
            'user': UserModel.objects.get(id=self.get_object().user_id),
            'quizzes': Quiz.objects.filter(author=self.get_object().user_id),
            'is_owner': is_owner,
        }

        return self.render_to_response(context)


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
