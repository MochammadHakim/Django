from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import BookAttribute, CustomUser, TransaksiPeminjaman
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import FormLogin, BookAttributeForm, FormPeminjaman, FormPengembalian
from django.conf import settings
from datetime import datetime
from django.contrib import messages
# Create your views here.

def is_staff(user):
    return user.is_authenticated and user.customuser.is_staff

def is_active(user):
    return user.is_authenticated

def home(request):
    books = BookAttribute.objects.all()
    transaksi = TransaksiPeminjaman.objects.all()  #\
    return render(request, 'base.html', {'books': books, 'transaksi': transaksi})

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
                return redirect('input')
            elif custom_user.is_active:
                login(request, user)
                return redirect('home')
        else:
            # Add an error message for incorrect credentials
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login/login.html', {'form':form})


@user_passes_test(is_staff)
def input(request):
    # Ambil semua objek BookAttribute
    books = BookAttribute.objects.all()

    if request.method == "POST":
        form = BookAttributeForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('input')  # Mengarahkan kembali ke halaman beranda setelah menyimpan
    else:
        form = BookAttributeForm()

    # Masukkan data buku ke dalam konteks saat merender template input.html
    return render(request, 'Admin/input.html', {'form': form, 'books': books})


def detailbook(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.user.is_authenticated:
        transaksi_list = TransaksiPeminjaman.objects.filter(buku=book, user=request.user)
    else:
        transaksi_list = []
    return render(request, 'detailbook.html', {'book': book, 'transaksi_list': transaksi_list})

def logoutadm(request):
    logout(request)
    request.session.flush()
    return redirect(home)
    
@user_passes_test(is_staff)
def book_edit(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.method == "POST":
        form = BookAttributeForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('input')
        else: 
            print("Form tidak Valid")
    else:
        form = BookAttributeForm(instance=book)
    return render(request, 'Admin/edit.html', {'form' : form})

@user_passes_test(is_staff)
def book_delete(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('input')
    return render(request, 'templates/library/book_confirm_delete.html', {'book': book})

@user_passes_test(is_active)
def borrow_book(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.method == 'POST':
        if book.status_peminjaman == 'available':
            transaksi = TransaksiPeminjaman.objects.create(buku=book, user=request.user)
            book.status_peminjaman = 'not-available'
            book.save()
            messages.success(request, 'Buku berhasil dipinjam.')
            return redirect('home')
        else:
            messages.error(request, 'Buku tidak tersedia.')
            return redirect('home')

@user_passes_test(is_active)
def return_book(request, transaksi_id):
    transaksi = get_object_or_404(TransaksiPeminjaman, pk=transaksi_id)
    if request.method == 'POST':
        # handle POST request logic here
        if transaksi.user == request.user:
            book = transaksi.buku
            book.status_peminjaman = 'available'
            book.save()
            transaksi.delete()
            return redirect('home')
        else:
            return redirect('home')
    
    return render(request, 'home', {'transaksi': transaksi})