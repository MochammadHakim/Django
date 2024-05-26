from django import forms
from django.contrib.auth.models import User
from .models import BookAttribute, TransaksiPeminjaman

class FormLogin(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'form-control'}),
    )

class BookAttributeForm(forms.ModelForm):
    class Meta:
        model = BookAttribute
        fields = [
            'judulBuku',
            'penulisBuku',
            'tahunTerbit',
            'kategoriBuku',
            'jumlahHalaman',
            'deskripsi',  # Tambahkan deskripsi ke dalam fields
            'coverBuku',
            'status_peminjaman',
        ]
        widgets = {
            'judulBuku': forms.TextInput(attrs={'class': 'form-control'}),
            'penulisBuku': forms.TextInput(attrs={'class': 'form-control'}),
            'tahunTerbit': forms.DateInput(attrs={'class': 'form-control w-50', 'type': 'date'}),
            'kategoriBuku': forms.TextInput(attrs={'class': 'form-control'}),
            'jumlahHalaman': forms.NumberInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),  # Widget untuk deskripsi
            'coverBuku': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status_peminjaman': forms.RadioSelect(choices=[
                ('available', 'Available'),
                ('not-available', 'Not Available')
            ], attrs={'class': 'form-check-input'}),
        }

class FormPeminjaman(forms.ModelForm):
    class meta:
        model = TransaksiPeminjaman
        fields = ['user', 'buku']

class FormPengembalian(forms.ModelForm):
    class Meta:
        model = TransaksiPeminjaman
        fields = ['buku']