from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

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

	def test_homepage_does_not_contain_incorrect_html(self):
		response = self.client.get("/")
		self.assertNotContains(response, "Hi there! I should not be on this page.")

	def test_homepage_url_resolves_homepageview(self):
		view = resolve("/")
		self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)