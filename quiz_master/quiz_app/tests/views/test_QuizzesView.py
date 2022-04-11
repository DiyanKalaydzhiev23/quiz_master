from django.urls import reverse
from quiz_master.quiz_app.tests.views.utils import SetUpMixin


class QuizzesViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('quizzes'))
        self.assertTemplateUsed(response, 'pages/quizzes.html')

    def test_get__all_quizzes_in_context__expect_success(self):
        response = self.client.get(reverse('quizzes'))
        quizzes = response.context['page_obj']

        self.assertEqual(2, len(quizzes))

    def test_post__math_quiz_in_context__expect_success(self):
        response = self.client.post(reverse('quizzes'), {'quiz_name': 'math'})
        quiz = response.context['page_obj']

        self.assertEqual(1, len(quiz))
