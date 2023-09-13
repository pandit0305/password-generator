import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(res):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length=10
    newPassword=''
    for x in range(length):
        newPassword += random.choice(chars)

    return render(res, 'myfirstsite/home.html',{'password':newPassword})

def about(res):
    return render(res, 'myfirstsite/about.html', {'name':'Pandit Gangadhar'})


def password(res):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if res.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXTZ'))

    if res.GET.get('numbers'):
        chars.extend(list('0123456789'))
    
    if res.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))


    length=int(res.GET.get('length',12))
    newPassword=''
    for x in range(length):
        newPassword += random.choice(chars)
    
    
    return render(res, 'myfirstsite/password.html' , {'password':newPassword})