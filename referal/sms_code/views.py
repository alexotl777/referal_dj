from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

class sms_code(TemplateView):
    template_name = "code.html"
    def get_pg(self, request):
        return render(request, self.template_name)