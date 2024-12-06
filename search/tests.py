from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class SearchPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = response = self.client.get(reverse("search"))
        self.assertTemplateUsed(response, "search.html")


class CreateGFEPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = response = self.client.get(reverse("create"))
        self.assertTemplateUsed(response, "create_gfe.html")
