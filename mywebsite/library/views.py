from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def loginadm(request):
    return render(request, 'login/admin.html')

def loginusr(request):
    return render(request, 'login/user.html')

def input(request):
    return render(request, 'Admin/input.html')

def detailbook(request):
    return render(request, 'detailbook.html')
    