from django.urls import reverse
from quiz_master.quiz_app.tests.views.utils import SetUpMixin


class SolveQuizViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user_two)
        response = self.client.get(reverse('solve quiz', kwargs={'pk': self.math_quiz.id}))
        self.assertTemplateUsed(response, 'pages/solve_quiz.html')
