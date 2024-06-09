"""moa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import write_seed_note, notes, note, send_seed_note, account_consent_boundary, set_account_consent_boundary, notifications, send_note
from core.views import room, index
from accounts.views import SignupPageView, ConfirmEmailPageView

urlpatterns = [
	# path("core/", include("core.urls"), name='core'),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls"), name="home"),
    # path("", index, name="home"),
    path("chat/<str:room_name>/", room, name="room"),
    path("accounts/signup/", SignupPageView.as_view(), name="account_signup"),
    path("accounts/confirm-email/", ConfirmEmailPageView.as_view(), name="account_email_confirm"),
    path("consent_boundary/", account_consent_boundary, name="account_consent_boundary"),
    path("notes/", notes, name="notes"),
    path("note/", note, name="note"),
    path("write", write_seed_note, name="write"),
    path("notifications/", notifications, name="notifications"),
    path("submit-note/", send_seed_note, name="send-seed-note"),
    path("note/send-note/", send_note, name="send-note"),
    path("consent_boundary/set/", set_account_consent_boundary, name="set-account-consent-boundary"),
]
