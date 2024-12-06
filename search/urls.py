#!/usr/bin/env python3

from django.urls import path

from .views import search_page_view, create_gfe_view

urlpatterns = [
    path("", search_page_view),
    path("create/", create_gfe_view),
]
