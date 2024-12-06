#!/usr/bin/env python3

from django.urls import path

from .views import search_page_view

urlpatterns = [
    path("", search_page_view)
]
