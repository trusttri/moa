from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

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


class AboutPageTests(SimpleTestCase):
	def setUp(self):
		url = reverse("about")
		self.response = self.client.get(url)

	def test_aboutpage_status_code(self):
		self.assertEqual(self.response.status_code, 200)

	def test_aboutpage_template(self):
		self.assertTemplateUsed(self.response, "about.html")

	def test_aboutpage_contains_correct_html(self):
		self.assertContains(self.response, "About Moa")

	def test_aboutpage_does_not_contain_incorret_html(self):
		self.assertNotContains(self.response, "Hi there! I should not be on this page.")

	def test_aboutpage_url_resolves_aboutpageview(self):
		view = resolve("/about/")
		self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
