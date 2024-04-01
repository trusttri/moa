from django.urls import path, include
from .views import SignupPageView


urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup")
]