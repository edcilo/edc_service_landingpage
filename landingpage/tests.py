from django.test import TestCase

from django.urls import reverse
from .models import Landing

# Create your tests here.
class HomeViewTests(TestCase):

    def test_load_home(self):
        response = self.client.get(reverse('landingpage:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "edcilo.com")


class LandingModelTests(TestCase):

    def test_first_landing_schema_created_should_be_published(self):
        schema = Landing.objects.create(name='test', schema={"title": "test"}, published=False)
        self.assertEqual(schema.published, True)

    def test_if_a_schema_is_published_others_schema_should_be_unpublished(self):
        test0 = Landing.objects.create(name='test_0', schema={"title": "Test O"}, published=True)
        test1 = Landing.objects.create(name='test_1', schema={"title": "Test 1"}, published=True)

        test0 = Landing.objects.get(name="test_0")
        schemas_published = Landing.objects.filter(published=True).count()
        self.assertEqual(test1.published, True)
        self.assertEqual(test0.published, False)
        self.assertEqual(schemas_published, 1)
