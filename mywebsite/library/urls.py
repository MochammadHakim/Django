from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path('input/', views.input, name='beranda'),
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('return-book/<int:transaksi_id>/', views.return_book, name='return_book'),
    # path('buku/create/', views.book_create, name='book_create'),
    path('buku/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('buku/<int:pk>/delete/', views.book_delete, name='book_delete'),

]
