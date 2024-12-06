from django.test import TestCase, SimpleTestCase

class SearchPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class CreateGFEPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)
