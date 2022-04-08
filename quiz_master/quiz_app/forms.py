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


class QuestionForm(forms.ModelForm):
    def __init__(self, quiz, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quiz = quiz

    def save(self, commit=True):
        question = super().save(commit=False)

        question.quiz = self.quiz
        if commit:
            question.save()

        return question

    class Meta:
        model = Question
        exclude = ('quiz',)


class AnswerForm(forms.ModelForm):
    def __init__(self, quiz, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quiz = quiz
        self.question = question

    def save(self, commit=True):
        answer = super().save(commit=False)

        answer.quiz = self.quiz
        answer.question = self.question

        if commit:
            answer.save()

        return answer

    class Meta:
        model = Answer
        exclude = ('quiz', 'question')


class StatsForm(forms.Form):
    total_questions = forms.IntegerField()
    average_time = forms.FloatField()
    correct_answers = forms.IntegerField()


QuestionFormSet = modelformset_factory(
    Question, fields=('question',), extra=1
)

AnswerFormSet = modelformset_factory(
    Answer, fields=('answer',), extra=1
)
