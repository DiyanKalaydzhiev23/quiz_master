from django.shortcuts import redirect
from django.views import generic as views
from quiz_master.quiz_app.forms import QuestionForm, AnswerForm, QuizForm, StatsForm
from quiz_master.quiz_app.models import Question, Answer


class GetQuizWithDataMixin(views.UpdateView):
    def get(self, *args, **kwargs):
        if 1 != len(self.request.user.groups.filter(name='moderator')):
            if self.get_object().author.id != self.request.user.id:
                return redirect('quizzes')

        questions_formset = []
        answers_formset = []

        for question in Question.objects.filter(quiz=self.get_object().id):
            questions_formset.append(QuestionForm(self.get_object(), instance=question))

        for answer in Answer.objects.filter(quiz=self.get_object().id):
            answers_formset.append(AnswerForm(
                self.get_object(), questions_formset[len(answers_formset)-1].save(commit=False), instance=answer)
            )

        context = {
            'pk': self.get_object().id,
            'stats_form': StatsForm(),
            'quiz_form': QuizForm(
                self.request.user,
                instance=self.get_object()
            ),
            'questions_formset': questions_formset,
            'answers_formset': answers_formset,
        }

        return self.render_to_response(context)
