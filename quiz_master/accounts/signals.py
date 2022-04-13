from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from quiz_master import settings


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def send_greeting_email(sender, instance, created, **kwargs):
    subject = "Registration greetings - Quiz Master"
    msg = f'Hello {instance.username},' \
          f'\n' \
          f'\n' \
          f"Thank you for your registration, let's learn and remember everything together." \
          f"\n" \
          f"\n" \
          f"Wish you all the best," \
          f"\n" \
          f"Quiz Master Team"

    to = instance.email
    send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
