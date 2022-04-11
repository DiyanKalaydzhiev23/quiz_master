from django.contrib.auth import get_user_model
from django.test import TestCase

from quiz_master.accounts.models import Profile
from quiz_master.quiz_app.models import Quiz, Question, Answer

UserModel = get_user_model()


class SetUpMixin(TestCase):
    def setUp(self):
        super().__init__()

        self.user_one = UserModel(
            username='Meto',
            password="metilab",
            email='di@metilab.com',
        )

        self.user_two = UserModel(
            username='Dido',
            password="didoldi",
            email='di@metilabprof.com',
        )

        self.user_one.full_clean()
        self.user_two.full_clean()

        self.user_one.save()
        self.user_two.save()

        self.profile_one = Profile(
            user=self.user_one
        )

        self.profile_two = Profile(
            user=self.user_two
        )

        self.profile_one.full_clean()
        self.profile_two.full_clean()

        self.profile_one.save()
        self.profile_two.save()

        self.biology_quiz = Quiz(
            category="biology",
            name="phagocytes",
            author=self.user_one,
        )

        self.math_quiz = Quiz(
            category="math",
            name="basic math",
            author=self.user_two,
        )

        self.biology_quiz.full_clean()
        self.math_quiz.full_clean()

        self.biology_quiz.save()
        self.math_quiz.save()

        self.one_plus_one_question = Question(
            quiz=self.math_quiz,
            question='1+1?',
        )

        self.one_plus_one_question.full_clean()
        self.one_plus_one_question.save()

        self.one_plus_one_answer = Answer(
            quiz=self.math_quiz,
            question=self.one_plus_one_question,
            answer='2',
        )

        self.one_plus_one_answer.full_clean()
        self.one_plus_one_answer.save()
