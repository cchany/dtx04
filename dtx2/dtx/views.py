from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

# Create your views here.


def Main(request):
    return render(request, 'dtx/main.html')