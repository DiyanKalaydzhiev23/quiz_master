# Generated by Django 4.0.3 on 2022-04-08 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='average_solving_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../../../media/default_image.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]