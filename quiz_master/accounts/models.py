from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from quiz_master.accounts.managers import QuizMasterUserManager
from django.db import models


class QuizMasterUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = QuizMasterUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        ),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='images',
        default='../../../media/images/default_image.png',
    )

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        QuizMasterUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    average_solving_time = models.FloatField(
        default=0,
    )

    accuracy = models.FloatField(
        default=0,
    )

    solved_quizzes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
