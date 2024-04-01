from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

	def test_homepage_url_name(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)

	def test_homepage_template(self):
		response = self.client.get("/")
		self.assertTemplateUsed(response, "home.html")