#!/usr/bin/env python3

from django.urls import path

from .views import SearchPageView, SearchResultsView, CreateGFEView

urlpatterns = [
    path("", SearchPageView.as_view(), name="search"),
    path("results/", SearchResultsView.as_view(), name="results"),
    path("create/", CreateGFEView.as_view(), name="create"),
]
