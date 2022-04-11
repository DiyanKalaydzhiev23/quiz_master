from django.contrib import admin
from django.contrib.auth import get_user_model

from quiz_master.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
