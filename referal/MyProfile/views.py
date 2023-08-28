from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

class viewProfile(TemplateView):
    template_name = "prof.html"
    def apply(request):
        print('hi')