from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView
import time
# Create your views here.

class sms_code(TemplateView):
    template_name = "code.html"
    time.sleep(2)
    def get_pg(self, request):
        time.sleep(2)
        return render(request, self.template_name)