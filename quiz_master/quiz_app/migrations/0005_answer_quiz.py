# Generated by Django 4.0.3 on 2022-03-30 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_alter_quiz_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quiz'),
            preserve_default=False,
        ),
    ]
