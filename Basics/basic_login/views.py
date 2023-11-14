from urllib import request
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render


# Create your views here.

def login_page(request):
    return render(request, 'login_page.html')

def landing_page(request):
    return render(request, 'index.html')

def my_image(request):
    img = open('basic_login/templates/images/sujan.jpeg', 'rb')
    response = FileResponse(img)
    return response

