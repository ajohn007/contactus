from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.DecimalField(max_digits=10, decimal_places=0)
    subject=models.TextField()
   
    def __str__(self):
        return self.name
