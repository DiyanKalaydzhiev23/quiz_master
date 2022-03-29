from json import loads
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from quiz_master.quiz_app.forms import QuizForm, QuestionFormSet, AnswerFormSet
from quiz_master.quiz_app.models import Quiz, Question, Answer


class QuizzesView(views.ListView):
    model = Quiz
    template_name = 'pages/quizzes.html'
    context_object_name = 'quizzes'


class AddQuizView(views.CreateView):
    template_name = "pages/add_quiz.html"

    def get(self, *args, **kwargs):
        context = {
            'quiz_form': QuizForm(self.request.user),
            'questions_formset': QuestionFormSet(queryset=Question.objects.none()),
            'answers_formset': AnswerFormSet(queryset=Answer.objects.none()),
        }

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        quiz_form_data = {
            'category': self.request.POST.get('category'),
            'name': self.request.POST.get('name'),
        }

        quiz_form = QuizForm(
            self.request.user,
            data=quiz_form_data,
        )

        if quiz_form.is_valid():
            quiz = quiz_form.save()

            question_formset = QuestionFormSet(data=self.request.POST)
            answers_formset = AnswerFormSet(data=self.request.POST)

            if question_formset.is_valid():
                questions = question_formset.save(commit=False)
                question_ids = []

                for question in questions:
                    question.quiz_id = quiz.id
                    question.save()
                    question_ids.append(question.id)

                if answers_formset.is_valid():
                    answers = answers_formset.save(commit=False)

                    for answer in answers:
                        answer.question_id = question_ids.pop(0)
                        answer.save()

                    return redirect(reverse_lazy('quizzes'))

            return self.get(self, *args, **kwargs)
