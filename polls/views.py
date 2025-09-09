from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponse # pyright: ignore[reportMissingModuleSource]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
