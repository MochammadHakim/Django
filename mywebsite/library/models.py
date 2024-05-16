from django.db import models

# Create your models here.

class BookAttribute(models.Model):
    judulBuku = models.CharField(max_length=120)
    tahunTerbit = models.IntegerField(null=False, default=0)
    penulisBuku = models.CharField(max_length=120, null=True, blank=True)
    kategoriBuku = models.CharField(max_length=120, null=True, blank=True)
    jumlahHalaman = models.IntegerField(null=False, default=0)
    coverBuku = models.ImageField(null=False, blank=True, upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.judulBuku