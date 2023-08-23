from django.forms import GenericIPAddressField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView
from authentication.models import authentication
# Create your views here.
import time

class authAPI(TemplateView):
    template_name = 'referal.html'
    queryset = authentication.objects.all()
    
    def code(request):
        if request.method == 'POST':
            phone_num = request.POST.get('num')
            # Выполнить необходимые действия с полученным значением
            # Записать данные в переменную или выполнить другую логику
            # ...
            print(phone_num)
            if len(phone_num) == 12 and phone_num[0] == '+' or len(phone_num) == 11 and phone_num[0] != '+':
                if phone_num[0] != '+':
                    phone_num = '+7' + phone_num[1:]
                try:
                    registration = authentication.objects.get(phone=phone_num)
                except authentication.DoesNotExist:
                    data = authentication(phone = phone_num)
                    data.save()
            else:
                return render(request, 'referal.html', {'format': 'Wrong format'})
            print(authentication.objects.all()[0], type(authentication.objects.all()[0]), type(phone_num))
            time.sleep(2)
        return render(request, 'code.html')