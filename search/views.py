from django.shortcuts import render
from django.http import HttpResponse

def search_page_view(request):
    return render(request, "search.html")

def create_gfe_view(request):
    return render(request, "create_gfe.html")
