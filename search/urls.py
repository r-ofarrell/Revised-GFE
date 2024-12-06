#!/usr/bin/env python3

from django.urls import path

from .views import SearchPageView, CreateGFEView

urlpatterns = [
    path("", SearchPageView.as_view()),
    path("create/", CreateGFEView.as_view()),
]
