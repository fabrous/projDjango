from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home (request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1', 't2', 't3']
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)