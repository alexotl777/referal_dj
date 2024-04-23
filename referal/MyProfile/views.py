from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView
from authentication.models import authentication

# Create your views here.

class ViewProfile(TemplateView):
    template_name = "prof.html"
    def apply(request):
        print('hi')

class Phones(TemplateView):
    queryset = authentication.objects.all()

    def getter(request):
        queryset = authentication.objects.all()
        phones_arr = list()
        for phone_obj in queryset:
            phones_arr.append(phone_obj.phone)

        return render(request, 'phones.html', {'phones_array': phones_arr})
        # return HttpResponse(phones_arr)