from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'news/home.html')


def sports(request):
    msg = [
        {"msg1": "jkdfhdsfkj"},
        {"msg2": "bdshjsdb"},
        {"msg3": "njvcklj"},
        {"msg4": "dxknf"}
    ]
    return render(request,'news/sports.html', {"msg": msg})

def business(request):
    return render(request,'news/business.html')

def entertainment(request):
    return render(request,'news/entertainment.html')