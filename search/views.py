from django.shortcuts import render
from django.http import HttpResponse

def search_page_view(request):
    return HttpResponse("Hello world!")
