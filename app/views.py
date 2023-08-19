from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def converter(request):
    return render(request, 'converter.html')
