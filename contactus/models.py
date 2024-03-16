from django.db import models

# Create your models here.

class Contactus(models.Model): 
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    level = models.IntegerField()
    comment = models.TextField()
    
    # screenshot = models.FileField(upload_to="screenshots/", blank=True)
    
    
    screenshot = models.ImageField(upload_to="screenshots/", blank=True)
