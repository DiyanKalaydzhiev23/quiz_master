# Generated by Django 4.0.3 on 2022-04-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_accuracy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='solved_quizzes',
            field=models.IntegerField(default=0),
        ),
    ]
