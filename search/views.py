from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import Client


class SearchPageView(TemplateView):
    template_name = "search.html"


class SearchResultsView(ListView):
    model = Client
    template_name = "search_results.html"

    def get_query(self):
        first_name = self.request.GET.get("first-name")
        last_name = self.request.GET.get("last-name")
        names_list = Client.objects.filter(
            Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name)
        )
        return names_list


class CreateGFEView(TemplateView):
    template_name = "create_gfe.html"
