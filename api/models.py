from django.db import models

# Create your models here.

class Sale(models.Model):
    department = models.CharField(max_length = 100)
    date = models.DateField()
  
    def __str__(self):
        return f"Sale: {self.department} - {self.date}"
    
class Department(models.Model):
    name = models.CharField(max_length= 50)