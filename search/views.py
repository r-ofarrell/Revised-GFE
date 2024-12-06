from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class SearchPageView(TemplateView):
    template_name = "search.html"

class CreateGFEView(TemplateView):
    template_name = "create_gfe.html"
