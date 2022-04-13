from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from quiz_master.accounts.forms import CreateProfileForm, EditProfileForm, EditUserForm
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from quiz_master.accounts.models import Profile
from quiz_master.common.quizzes_get_view_and_context import get


UserModel = get_user_model()


@login_required()
def profile_view(request, pk=None, quiz_name=None):
    if request.method == 'GET':
        return get(request, pk, quiz_name, 'accounts/profile.html')
    else:
        return get(request, pk, request.POST.get('quiz_name'), 'accounts/profile.html')


class EditProfile(LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'

    def get(self, *args, **kwargs):
        context = {
            'user_form': EditUserForm(instance=UserModel.objects.get(pk=self.get_object().user_id)),
            'profile_form': EditProfileForm(instance=self.get_object()),
        }

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        user_data = {
            'username': self.request.POST.get('username'),
            'email': self.request.POST.get('email'),
        }

        profile_data = {
            'first_name': self.request.POST.get('first_name'),
            'last_name': self.request.POST.get('last_name'),
        }

        user_form = EditUserForm(
            data=user_data,
            instance=UserModel.objects.get(pk=self.get_object().user_id),
        )

        profile_form = EditProfileForm(
            data=profile_data,
            files=self.request.FILES,
            instance=self.get_object()
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile', self.get_object().user_id)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'form_errors': user_form.errors.update(profile_form.errors.items()),
        }

        return self.render_to_response(context)


class DeleteUserView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'pages/delete_profile.html'
    success_url = reverse_lazy('home')


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


class UserLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    success_url = reverse_lazy('login')
