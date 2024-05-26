from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class BookAttribute(models.Model):
    judulBuku = models.CharField(max_length=255)
    penulisBuku = models.CharField(max_length=255, blank=True, null=True)
    # --- FORMAT TAHUN TERBIT = YYYY-MM-DD
    tahunTerbit = models.DateField()
    kategoriBuku = models.CharField(max_length=255, blank=True, null=True)
    jumlahHalaman = models.IntegerField()
    coverBuku = models.ImageField(upload_to='covers/')
    status_peminjaman = models.CharField(max_length=20, null=False, blank=True, choices=[
        ('available', 'Available'),
        ('not-available', 'Not Available'),
    ])
    def __str__(self):
        return self.judulBuku
    
class TransaksiPeminjaman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(BookAttribute, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateTimeField(default=datetime.now)
    tanggal_kembali = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.buku.Judulbuku}"
