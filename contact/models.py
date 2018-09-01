from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 100, verbose_name="İsim Soyisim")
    email = models.EmailField()
    message = models.TextField(max_length= 3000, verbose_name= "Mesajınız")
    sending_date = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")
