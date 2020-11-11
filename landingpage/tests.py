from django.test import TestCase

from django.urls import reverse

# Create your tests here.
class HomeViewTests(TestCase):

    def test_load_home(self):
        response = self.client.get(reverse('landingpage:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "edcilo.com")
