from django import forms
from django.contrib.auth.models import User
from .models import BookAttribute
from .models import TransaksiPeminjaman


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
            'coverBuku',
            'status_peminjaman'
        ]

class FormPeminjaman(forms.ModelForm):
    class meta:
        model = TransaksiPeminjaman
        fields = ['user', 'buku']

class FormPengembalian(forms.ModelForm):
    class Meta:
        model = TransaksiPeminjaman
        fields = ['buku']