from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self): 
        return f"{self.name}"


class Student(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(100)])
    email = models.EmailField()
    phone = models.CharField(max_length=254,null=True)
    is_registered = models.BooleanField(default=False)
    date_joined = models.DateField(null=True)
    
    
    # relate student with the Mentor (1-to-Many)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    
    courses = models.ManyToManyField(Course)
    
    
    def __str__(self): 
        return f"{self.first_name}"


class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mentor_number = models.IntegerField()
    
    bank_details = models.OneToOneField('BankDetails', on_delete=models.PROTECT, null=True)
    
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"

class BankDetails(models.Model): 
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=250)
    bank_name = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = "Bank Details"
        
    def __str__(self): 
        return f"{self.bank_name} {self.account_number}"
    

    
    

