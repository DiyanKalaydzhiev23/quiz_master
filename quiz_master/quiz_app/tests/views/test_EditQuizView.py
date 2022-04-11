from django.urls import reverse
from quiz_master.quiz_app.forms import StatsForm, QuizForm
from quiz_master.quiz_app.models import Question
from quiz_master.quiz_app.tests.views.utils import SetUpMixin


class EditQuizViewTests(SetUpMixin):
    def test_get_expected_template(self):
        self.client.force_login(self.user_two)
        response = self.client.get(reverse('edit quiz', kwargs={'pk': self.user_two.pk}))
        self.assertTemplateUsed(response, 'pages/edit_quiz.html')

    def test_get_context_expect_success(self):
        self.client.force_login(self.user_two)
        response = self.client.get(reverse('edit quiz', kwargs={'pk': self.user_two.pk}))

        self.assertEqual(self.user_two.pk, response.context['pk'])
        self.assertEqual(StatsForm, type(response.context['stats_form']))
        self.assertEqual(QuizForm, type(response.context['quiz_form']))
        self.assertEqual(1, len(response.context['questions_formset']))
        self.assertEqual(1, len(response.context['answers_formset']))

    def test_post_expect_updating_quiz(self):
        self.client.force_login(self.user_two)

        response = self.client.post(reverse('edit quiz', kwargs={'pk': self.user_two.pk}), {
                'category': ['math'],
                'name': ['basic math'],
                'question0': ['1+1?'],
                'answer0': ['2'],
                'question1': ['2+2?'],
                'answer1': ['4'],
                'question2': ['3+3?'],
                'answer2': ['6'],
                'question3': ['4+4?'],
                'answer3': ['8']
            }
        )

        self.assertEqual(1, len(Question.objects.filter(question='4+4?')))
