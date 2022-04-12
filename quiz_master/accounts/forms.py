from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from quiz_master.accounts.models import Profile


class CustomUserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class CustomUserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class CreateProfileForm(auth_forms.UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = auth_forms.UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
