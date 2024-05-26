from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path('input/', views.input, name='beranda'),
    path('buku/<int:pk>/pinjam/', views.pinjam_buku, name='pinjam_buku'),
    path('kembalikan/<int:pk>/', views.kembalikan_buku, name='kembalikan_buku'),
    # path('buku/create/', views.book_create, name='book_create'),
    path('buku/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('buku/<int:pk>/delete/', views.book_delete, name='book_delete'),

]
