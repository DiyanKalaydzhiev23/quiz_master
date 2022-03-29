from django import forms
from django.forms import modelformset_factory
from quiz_master.quiz_app.models import Quiz, Question, Answer


class QuizForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        quiz = super().save(commit=False)

        quiz.author = self.user
        if commit:
            quiz.save()

        return quiz

    class Meta:
        model = Quiz
        exclude = ('author',)


QuestionFormSet = modelformset_factory(
    Question, fields=('question',), extra=1
)

AnswerFormSet = modelformset_factory(
    Answer, fields=('answer',), extra=1
)
