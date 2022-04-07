from django.contrib.auth import forms as auth_forms, get_user_model


class CreateProfileForm(auth_forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
