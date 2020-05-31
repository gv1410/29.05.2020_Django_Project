from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
import datetime
# Create your views here.

def test(request):
    req = requests.get('https://www.nbrb.by/api/exrates/rates/298?ondate=2016-7-05')
    result = req.json()
    rate = result.get('Cur_OfficialRate')
    r = random.randint(0, 100)
    data = [1, 3, 6, 5, 8, 77, 8]

    date = datetime.datetime.now()

    context = {'some_value': r, 'rate': rate, 'my_data': data, 'now': date}
    return render(request, template_name='testapp/test.html', context=context)