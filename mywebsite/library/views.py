from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookAttribute, CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import FormLogin
from django.conf import settings
# Create your views here.

def is_staff(user):
    return user.is_authenticated and user.customuser.is_staff
def home(request):
    return render(request, 'base.html')

def loginadm(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            custom_user = CustomUser.objects.get(user=user)
            if custom_user.is_staff:
                login(request, user)
                return redirect('/login/admin.html/input.html')
            elif custom_user.is_active:
                login(request, user)
                return redirect('/home')
    return render(request, 'login/admin.html', {'form':form})

def loginusr(request):
    return render(request, 'login/user.html')

@user_passes_test(is_staff)
def input(request):
    return render(request, 'Admin/input.html')

def detailbook(request):
    return render(request, 'detailbook.html')

def logoutadm(request):
    logout(request)
    request.session.flush()
    return redirect('/home')

def home(request):
    all_books = BookAttribute.objects.all
    return render(request, 'base.html', {'all':all_books})
    # return render(request, 'base.html')
# def LibraryList(request):
#     all_books = LibraryList.objects.all
#     return render(request, 'base.html', {'all':all_books})
#     # return render(request, 'base.html')

