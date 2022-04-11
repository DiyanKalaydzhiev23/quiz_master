from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from quiz_master.quiz_app.models import Quiz


UserModel = get_user_model()


class QuizModelTests(TestCase):
    def setUp(self):
        self.user = UserModel(
            username='Meto',
            password="metilab",
            email='di@metilab.com',
        )

        self.user.full_clean()
        self.user.save()

    def test_quiz_model_create__with_valid_data__expect_success(self):
        quiz_instance = Quiz(
            category="biology",
            name="phagocytes",
            author=self.user,
        )

        quiz_instance.full_clean()
        quiz_instance.save()

        self.assertIsNotNone(quiz_instance.pk)

    def test_quiz_model__with_invalid_name__expect_fail(self):
        name = 'n' * 151

        quiz_instance = Quiz(
            category="biology",
            name=name,
            author=self.user,
        )

        with self.assertRaises(ValidationError) as context:
            quiz_instance.full_clean()
            quiz_instance.save()

        self.assertIsNotNone(context.exception)
