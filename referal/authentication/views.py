from django.forms import GenericIPAddressField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView
from authentication.models import authentication
# Create your views here.

class authAPI(TemplateView):
    template_name = 'referal.html'
    queryset = authentication.objects.all()
    def form_phone(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)