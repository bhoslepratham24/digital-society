from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Emergency_Contact(models.Model):

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)


    def __str__(self):
        return self.name+' '+self.occupation

