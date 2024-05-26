from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import BookAttribute, CustomUser, TransaksiPeminjaman
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import FormLogin, BookAttributeForm, FormPeminjaman, FormPengembalian
from django.conf import settings
from datetime import datetime
# Create your views here.

def is_staff(user):
    return user.is_authenticated and user.customuser.is_staff

def is_active(user):
    return user.is_authenticated

def home(request):
    books = BookAttribute.objects.all()
    return render(request, 'base.html', {'books': books})

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
                return redirect(input)
            elif custom_user.is_active:
                login(request, user)
                return redirect(home)
    return render(request, 'login/login.html', {'form':form})

@user_passes_test(is_staff)
def input(request):
    # Ambil semua objek BookAttribute
    books = BookAttribute.objects.all()

    if request.method == "POST":
        form = BookAttributeForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('home')  # Mengarahkan kembali ke halaman beranda setelah menyimpan
    else:
        form = BookAttributeForm()

    # Masukkan data buku ke dalam konteks saat merender template input.html
    return render(request, 'Admin/input.html', {'form': form, 'books': books})


def detailbook(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    return render(request, 'detailbook.html', {'book':book})

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
def pinjam_buku(request):
    if request.method == 'POST':
        form = FormPeminjaman(request.POST)
        if form.is_valid():
            transaksi_peminjaman = form.save(commit=False)
            buku = transaksi_peminjaman.buku
            if buku.status_peminjaman == 'available':
                buku.status_peminjaman == 'not-available'
                buku.save()
                transaksi_peminjaman.save()
                return redirect('daftar_buku')
    
    else:
        form = FormPeminjaman()
    return render(request, 'pinjam_buku.html', {'form' : form})

@user_passes_test(is_active)
def kembalikan_buku(request, transaksi_id):
    transaksi = get_object_or_404(TransaksiPeminjaman, id=transaksi_id)
    if request.method == 'POST':
        form = FormPengembalian(request.POST, instance=transaksi_id)
        if form.is_valid():
            buku = transaksi.buku
            buku.status_peminjaman = 'available'
            buku.save()
            transaksi.tanggal_kembali = datetime.now()
            transaksi.save()
            return redirect('daftar_buku')
    
    else:
        form = FormPengembalian(instance=transaksi)
    return render(request, 'kembalikan_buku.html', {'form': form})