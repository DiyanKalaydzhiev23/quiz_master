from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from quiz_master.accounts.models import Profile
from quiz_master.common.quizzes_get_view_and_context import get
from quiz_master.quiz_app.forms import QuizForm, QuestionFormSet, AnswerFormSet, QuestionForm, AnswerForm
from quiz_master.quiz_app.mixins import GetQuizWithDataMixin
from quiz_master.quiz_app.models import Quiz, Question, Answer


def quizzes_view(request, pk=None, quiz_name=None):
    if request.method == 'GET':
        return get(request, pk, quiz_name, 'pages/quizzes.html')
    else:
        return get(request, pk, request.POST.get('quiz_name'), 'pages/quizzes.html')


class LandingView(views.TemplateView):
    template_name = 'landing_page.html'


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

        question_formset = QuestionFormSet(data=self.request.POST)
        answers_formset = AnswerFormSet(data=self.request.POST)

        if quiz_form.is_valid() and question_formset.is_valid() and answers_formset.is_valid():
            quiz = quiz_form.save()

            questions = question_formset.save(commit=False)
            question_ids = []

            for question in questions:
                question.quiz_id = quiz.id
                question.save()
                question_ids.append(question.id)

            answers = answers_formset.save(commit=False)

            for answer in answers:
                answer.quiz_id = quiz.id
                answer.question_id = question_ids.pop(0)
                answer.save()

            profile = Profile.objects.get(user_id=self.request.user.id)
            profile.created_quizzes += 1
            profile.save()

            return redirect(reverse_lazy('quizzes'))

        quiz_form_data = {
            'category': self.request.POST.get('category'),
            'name': self.request.POST.get('name'),
        }

        context = {
            'quiz_form': QuizForm(
                self.request.user,
                data=quiz_form_data,
            ),
            'questions_formset': QuestionFormSet(self.request.POST),
            'answers_formset': AnswerFormSet(self.request.POST),
        }

        return self.render_to_response(context)


class EditQuizView(GetQuizWithDataMixin, views.UpdateView):
    model = Quiz
    template_name = "pages/edit_quiz.html"

    def post(self, *args, **kwargs):
        quiz_form_data = {
            'category': self.request.POST.get('category'),
            'name': self.request.POST.get('name'),
        }

        quiz_form = QuizForm(
            self.request.user,
            data=quiz_form_data,
            instance=self.get_object()
        )

        if quiz_form.is_valid():
            quiz = quiz_form.save()

            questions_formset = [q for q in Question.objects.filter(quiz=self.get_object().id)]
            answers_formset = [a for a in Answer.objects.filter(quiz=self.get_object().id)]

            questions_list = [self.request.POST.get(f'question{i}') for i in range(0, (len(self.request.POST.dict())-2) // 2)]

            for i in range(0, (len(self.request.POST.dict())-2) // 2):
                question_form = QuestionForm(
                    quiz,
                    data={f'question': questions_list[i]},
                    instance=questions_formset[i] if i < len(questions_formset) else None,
                )

                if question_form.is_valid():
                    question = question_form.save()

                    if i >= len(questions_formset):
                        questions_formset.append(question)

            if len(questions_list) < len(questions_formset):
                for i in range(len(questions_formset)-1, len(questions_list)-1, -1):
                    questions_formset[i].delete()

            for i in range(0, ((len(self.request.POST.dict())-2) // 2)):
                answer_form = AnswerForm(
                    quiz,
                    questions_formset[i],
                    data={f'answer': self.request.POST.get(f'answer{i}')},
                    instance=answers_formset[i] if i < len(answers_formset) else None,
                )

                if answer_form.is_valid():
                    answer_form.save()

            return redirect(reverse_lazy('quizzes'))

        return self.get(self, *args, **kwargs)


class DeleteQuizView(views.DeleteView):
    model = Quiz
    template_name = 'pages/delete_quiz.html'
    success_url = reverse_lazy('quizzes')


class SolveQuizView(GetQuizWithDataMixin, views.UpdateView):
    model = Quiz
    template_name = "pages/solve_quiz.html"

    def post(self, *args, **kwargs):
        accuracy = int(self.request.POST.get('correct_answers')) / int(self.request.POST.get('total_questions')) * 100
        profile = Profile.objects.filter(user_id=self.request.user.id)[0]

        if profile.average_solving_time:
            profile.average_solving_time = (profile.average_solving_time + float(self.request.POST.get('average_time'))) / 2
        else:
            profile.average_solving_time = float(self.request.POST.get('average_time'))

        if profile.accuracy:
            profile.accuracy = (profile.accuracy + accuracy) / 2
        else:
            profile.accuracy = accuracy

        profile.solved_quizzes += 1

        profile.save()

        return redirect(reverse_lazy('quizzes'))
