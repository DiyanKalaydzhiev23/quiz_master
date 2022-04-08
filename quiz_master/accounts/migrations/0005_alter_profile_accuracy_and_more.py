# Generated by Django 4.0.3 on 2022-04-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_accuracy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='accuracy',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='average_solving_time',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
