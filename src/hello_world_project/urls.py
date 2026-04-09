# src/hello_world_project/urls.py
from django.contrib import admin
from django.urls import path, include  # <<< neu

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # <<< neu
]