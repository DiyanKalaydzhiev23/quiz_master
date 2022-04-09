from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Quiz(models.Model):
    TYPE_CHOICE_BIOLOGY = 'biology'
    TYPE_CHOICE_CHEMISTRY = 'chemistry'
    TYPE_CHOICE_PHYSICS = 'physics'
    TYPE_CHOICE_INFORMATION_TECHNOLOGIES = 'information technologies'
    TYPE_CHOICE_MATH = 'math'
    TYPE_CHOICE_LANGUAGES = 'languages'
    TYPE_CHOICE_LITERATURE = 'literature'
    TYPE_CHOICES_MUSIC = 'music'
    TYPE_CHOICES_ART = 'art'
    TYPE_CHOICES_HISTORY = 'history'
    TYPE_CHOICES_GEOGRAPHY = 'geography'
    TYPE_CHOICES_PHILOSOPHY = 'philosophy'
    TYPE_CHOICES_OTHER = 'other'

    TYPE_CHOICES = (
        (TYPE_CHOICE_BIOLOGY, 'Biology'),
        (TYPE_CHOICE_CHEMISTRY, 'Chemistry'),
        (TYPE_CHOICE_PHYSICS, 'Physics'),
        (TYPE_CHOICE_INFORMATION_TECHNOLOGIES, 'Information Technologies'),
        (TYPE_CHOICE_MATH, 'Math'),
        (TYPE_CHOICE_LANGUAGES, 'Languages'),
        (TYPE_CHOICE_LITERATURE, 'Literature'),
        (TYPE_CHOICES_MUSIC, 'Music'),
        (TYPE_CHOICES_ART, 'Art'),
        (TYPE_CHOICES_HISTORY, 'History'),
        (TYPE_CHOICES_GEOGRAPHY, 'Geography'),
        (TYPE_CHOICES_PHILOSOPHY, 'Philosophy'),
        (TYPE_CHOICES_OTHER, 'Other'),
    )

    category = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES_OTHER,
    )

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
    )

    question = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return f"{self.question}"


class Answer(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    answer = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return f"{self.answer}"
