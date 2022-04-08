from django.contrib.auth import forms as auth_forms, get_user_model
from quiz_master.accounts.models import Profile


class CreateProfileForm(auth_forms.UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
