# Generated by Django 4.0.3 on 2022-04-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='accuracy',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
