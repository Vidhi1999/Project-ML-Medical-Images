from django.db import models

# Create your models here.
'''class user(models.Model):
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 254)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)'''

class upload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    #document = models.FileField(upload_to='documents/')
    medical_image = models.ImageField(upload_to = 'images/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)


