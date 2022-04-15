from django.contrib.auth import get_user_model
from django.urls import reverse

from quiz_master.accounts.models import Profile
from quiz_master.common.utils import SetUpMixin


class EditProfileViewTest(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user_two)
        response = self.client.get(reverse('edit profile', kwargs={'pk': self.user_two.pk}))
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_get__correct_context(self):
        self.client.force_login(self.user_two)
        response = self.client.get(reverse('edit profile', kwargs={'pk': self.user_two.pk}))

        self.assertIsNotNone(response.context['user_form'])
        self.assertIsNotNone(response.context['profile_form'])

    def test_post__expect_correct_data_to_be_saved(self):
        self.client.force_login(self.user_two)
        self.client.post(reverse('edit profile', kwargs={'pk': self.user_two.pk}), {
            'username': 'SashoAx',
            'email': 'sasho123@gmail.com',
            'first_name': 'Sasho',
            'last_name': 'Axolotlski',
        })

        self.assertEqual(1, len(get_user_model().objects.filter(username="SashoAx")))
        self.assertEqual(1, len(get_user_model().objects.filter(email="sasho123@gmail.com")))
        self.assertEqual(1, len(Profile.objects.filter(first_name="Sasho")))
        self.assertEqual(1, len(Profile.objects.filter(last_name="Axolotlski")))
