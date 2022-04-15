from django.urls import reverse
from quiz_master.quiz_app.models import Quiz
from quiz_master.common.utils import SetUpMixin


class AddQuizTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user_one)
        response = self.client.get(reverse('add quiz'))
        self.assertTemplateUsed(response, 'pages/add_quiz.html')

    def test_get__expect_quiz_form_in_context(self):
        self.client.force_login(self.user_one)
        response = self.client.get(reverse('add quiz'))
        form = response.context['quiz_form']

        self.assertIsNotNone(form)

    def test_get__expect_questions_formset_in_context(self):
        self.client.force_login(self.user_one)
        response = self.client.get(reverse('add quiz'))
        questions_formset = response.context['questions_formset']

        self.assertIsNotNone(questions_formset)

    def test_get_expect_answer_formset_in_context(self):
        self.client.force_login(self.user_one)
        response = self.client.get(reverse('add quiz'))
        answer_formset = response.context['answers_formset']

        self.assertIsNotNone(answer_formset)

    def test_post_expect_saved_quiz(self):
        self.client.force_login(self.user_one)

        response = self.client.post(reverse('add quiz'), {
                'category': 'math',
                'name': 'basic math 2',
                'form-TOTAL_FORMS': ['1', '1'],
                'form-INITIAL_FORMS': ['0', '0'],
                'form-MIN_NUM_FORMS': ['0', '0'],
                'form-MAX_NUM_FORMS': ['1000', '1000'],
                'form-0-question': ['5+5?'],
                'form-0-id': ['', ''],
                'form-0-answer': ['10']
            }
        )

        quizzes = Quiz.objects.filter(name='basic math 2')
        self.assertEqual(1, len(quizzes))
