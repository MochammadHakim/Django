from django.shortcuts import render
from django.http import HttpResponse
from .models import BookAttribute

# Create your views here.
def home(request):
    all_books = BookAttribute.objects.all
    return render(request, 'base.html', {'all':all_books})
    # return render(request, 'base.html')

# def LibraryList(request):
#     all_books = LibraryList.objects.all
#     return render(request, 'base.html', {'all':all_books})
#     # return render(request, 'base.html')