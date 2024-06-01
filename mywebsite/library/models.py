from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class BookAttribute(models.Model):
    judulBuku = models.CharField(max_length=255)
    penulisBuku = models.CharField(max_length=255, blank=True, null=True)
    tahunTerbit = models.DateField()
    kategoriBuku = models.CharField(max_length=255, blank=True, null=True)
    jumlahHalaman = models.IntegerField()
    coverBuku = models.ImageField(upload_to='covers/')
    deskripsi = models.TextField(blank=True, null=True)  # Tambahkan bidang deskripsi
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
    
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_staff']
    list_filter = ['is_staff']
    search_fields = ['user__username']

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    else:
        instance.customuser.save()