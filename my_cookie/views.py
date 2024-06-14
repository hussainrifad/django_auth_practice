from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
myToken = 'adagfkahgfauyg12134a23e3j34j'

def set_browser_cookie(request):
    res = render(request, 'setcookie.html')
    res.set_cookie('token', myToken, expires=datetime.utcnow()+timedelta(days=7))
    return res

def get_browser_cookie(request):
    token = request.COOKIES.get('token')
    return render(request, 'getcookie.html', {'token':token})

def del_browser_cookie(request):
    res = render(request, 'delcookie.html')
    res.delete_cookie('token')
    return res

def 