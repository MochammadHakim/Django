from django.db import models

# Create your models here.

class BookAttribute(models.Model):
    judulBuku = models.CharField(max_length=255)
    penulisBuku = models.CharField(max_length=255, blank=True, null=False)
    # --- FORMAT TAHUN TERBIT = YYYY-MM-DD
    tahunTerbit = models.DateField()
    kategoriBuku = models.CharField(max_length=255, blank=True, null=False)
    jumlahHalaman = models.IntegerField()
    coverBuku = models.ImageField(upload_to='covers/')
    status_peminjaman = models.CharField(max_length=20, null=False, blank=True, choices=[
        ('available', 'Available'),
        ('not-available', 'Not Available'),
    ])
    def __str__(self):
        return self.judulBuku