from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BookAttribute
from .forms import BookAttributeForm
from django.contrib.auth import authenticate, login, logout
from .forms import FormLogin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import BookAttribute, TransaksiPeminjaman
from .forms import FormPeminjaman, FormPengembalian
from datetime import datetime
# Create your views here.
def home(request):
    return render(request, 'base.html')

def loginadm(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login/admin.html/input.html')
    return render(request, 'login/admin.html', {'form':form})

def loginusr(request):
    return render(request, 'login/user.html')

@login_required(login_url=settings.LOGIN_URL)
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

def book_list(request):
    books = BookAttribute.objects.all()
    return render(request, 'templates/library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    return render(request, 'templates/library/book_detail.html', {'book':book})


def book_create(request):
    if request.method == "POST":
        form = BookAttributeForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('book_list')  # Mengarahkan kembali tanpa argumen kata kunci
    else:
        form = BookAttributeForm()
    return render(request, 'templates/library/book_form.html', {'form':form})

    
def book_edit(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.method == "POST":
        form = BookAttributeForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
        else: 
            print("Form tidak Valid")
    else:
        form = BookAttributeForm(instance=book)
    return render(request, 'templates/library/book_form.html', {'form' : form})





    
def book_delete(request, pk):
    book = get_object_or_404(BookAttribute, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'templates/library/book_confirm_delete.html', {'book': book})

@login_required
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

@login_required
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