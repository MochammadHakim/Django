from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
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