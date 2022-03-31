from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from quiz_master.quiz_app.forms import QuizForm, QuestionFormSet, AnswerFormSet, QuestionForm, AnswerForm
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


class EditQuizView(views.UpdateView):
    model = Quiz
    template_name = "pages/edit_quiz.html"

    def get(self, *args, **kwargs):
        questions_formset = []
        answers_formset = []

        for question in Question.objects.filter(quiz=self.get_object().id):
            questions_formset.append(QuestionForm(self.get_object(), instance=question))

        for answer in Answer.objects.filter(quiz=self.get_object().id):
            answers_formset.append(AnswerForm(
                self.get_object(), questions_formset[len(answers_formset)].save(commit=False), instance=answer)
            )

        context = {
            'pk': self.get_object().id,
            'quiz_form': QuizForm(
                self.request.user,
                instance=self.get_object()
            ),
            'questions_formset': questions_formset,
            'answers_formset': answers_formset,
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
            instance=self.get_object()
        )

        if quiz_form.is_valid():
            quiz = quiz_form.save()

            questions_formset = [q for q in Question.objects.filter(quiz=self.get_object().id)]
            answers_formset = [a for a in Answer.objects.filter(quiz=self.get_object().id)]

            answers_list = [self.request.POST.get(f'answer{i}') for i in range(0, len(self.request.POST.dict())-6)]

            for i in range(0, len(self.request.POST.dict())-6):
                question_form = QuestionForm(
                    quiz,
                    data={f'question': self.request.POST.get(f'question{i}')},
                    instance=questions_formset[i] if i < len(questions_formset) else None,
                )

                if question_form.is_valid():
                    question = question_form.save()

                    if i >= len(questions_formset)-1:
                        questions_formset.append(question)

            for i in range(0, len(self.request.POST.dict()) - 6):
                answer_form = AnswerForm(
                    quiz,
                    questions_formset[i],
                    data={f'answer': self.request.POST.get(f'answer{i}')},
                    instance=answers_formset[i] if i < len(answers_formset) else None,
                )

                if answer_form.is_valid():
                    answer_form.save()

            return redirect(reverse_lazy('quizzes'))

        # question_formset = QuestionFormSet(initial=self.request.POST)
        # answers_formset = AnswerFormSet(initial=self.request.POST)
        #
        # if quiz_form.is_valid() and answers_formset.is_valid():
        #     quiz = quiz_form.save()
        #
        #     questions = question_formset.save(commit=False)
        #     question_ids = []
        #
        #     for question in questions:
        #         question.quiz_id = quiz.id
        #         question.save()
        #         question_ids.append(question.id)
        #
        #     answers = answers_formset.save(commit=False)
        #
        #     for answer in answers:
        #         answer.quiz_id = quiz.id
        #         answer.question_id = question_ids.pop(0)
        #         answer.save()
        #

        # quiz_form_data = {
        #     'category': self.request.POST.get('category'),
        #     'name': self.request.POST.get('name'),
        # }
        #
        # context = {
        #     'pk': self.get_object().id,
        #     'quiz_form': QuizForm(
        #         self.request.user,
        #         data=quiz_form_data,
        #     ),
        #     'questions_formset': QuestionFormSet(self.request.POST),
        #     'answers_formset': AnswerFormSet(self.request.POST),
        # }

        return self.get(self, *args, **kwargs)
