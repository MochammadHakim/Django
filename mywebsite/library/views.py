from django.shortcuts import render
from django.http import HttpResponse
from .models import BookAttribute

# Create your views here.
def home(request):
<<<<<<< HEAD
    return render(request, 'base.html')

def loginadm(request):
    return render(request, 'login/admin.html')

def loginusr(request):
    return render(request, 'login/user.html')

def input(request):
    return render(request, 'Admin/input.html')

def detailbook(request):
    return render(request, 'detailbook.html')
    
=======
    all_books = BookAttribute.objects.all
    return render(request, 'base.html', {'all':all_books})
    # return render(request, 'base.html')

# def LibraryList(request):
#     all_books = LibraryList.objects.all
#     return render(request, 'base.html', {'all':all_books})
#     # return render(request, 'base.html')
>>>>>>> 671d48398833dfc3d34ea0bfded2ce62cd3f5794
