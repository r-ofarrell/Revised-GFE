from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db.models import Q, Count
from django.views.generic import TemplateView, ListView

from .models import Client, Estimate, EstimateServiceDetails


class EstimateRenewalUpcomingView(ListView):
    model = Estimate
    template_name = "upcoming_renewals.html"

    def get_query(self):
        pass


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


class ClientEstimatesView(ListView):
    template_name = "client_estimates.html"

    def get_queryset(self):
        self.client = get_object_or_404(Client, name=self.kwargs["id"])
        return Estimate.objects.filter(client=self.client)


class CreateNewClientView(TemplateView):
    template_name = "create_client.html"


class CreateGFEView(TemplateView):
    template_name = "create_gfe.html"
