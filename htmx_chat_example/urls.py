"""
URL configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from htmx_chat_example.views import ChatView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("chat/", ChatView.as_view(), name="chat"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
