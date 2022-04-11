from django.test import TestCase
from django.urls import reverse


class LandingViewTests(TestCase):
    def test_get_correct_template_expect_success(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'landing_page.html')
