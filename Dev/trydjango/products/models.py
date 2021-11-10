from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=125) #panjang maximal = harus diisi
    description = models.TextField(blank=True, null=True) #tidak diisi tidak apa apa
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField()

#Setiap saat mengganti models.py tulis kode dibawah di terminal
#python manage.py makemigrations
#python manage.py migrate
