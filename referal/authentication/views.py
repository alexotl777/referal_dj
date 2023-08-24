from django.forms import GenericIPAddressField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import TemplateView
from authentication.models import authentication
# Create your views here.
import random
import string
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
            
            if len(phone_num) == 12 and phone_num[0] == '+' or len(phone_num) == 11 and phone_num[0] != '+':
                if phone_num[0] != '+':
                    phone_num = '+7' + phone_num[1:]
                try:
                    registration = authentication.objects.get(phone=phone_num)
                except authentication.DoesNotExist:
                    # задаем набор символов для генерации кода
                    characters = string.ascii_uppercase + string.digits + string.ascii_lowercase

                    # генерируем случайный 6-значный код
                    code_rnd = ''.join(random.choice(characters) for i in range(6))
                    data = authentication(phone = phone_num, invite=code_rnd)
                    data.save()
            else:
                return render(request, 'referal.html', {'format': 'Wrong format'})
            
            time.sleep(2)
        return render(request, 'code.html')