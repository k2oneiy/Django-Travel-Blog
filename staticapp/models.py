from django.db import models

# Create your models here.

class Denination(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    content=models.CharField(max_length=500)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)
    
