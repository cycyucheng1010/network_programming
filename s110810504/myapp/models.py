from django.db import models

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=20 , null = False)
    Sex = models.CharField(max_length=2,default='M',null = False)
    Birth = models.DateField(null = False)
    Email = models.CharField(max_length=100,blank = True ,null =False,default='')
    Phone = models.CharField(max_length=50,blank=True,default='')
    Home_Address = models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.Name