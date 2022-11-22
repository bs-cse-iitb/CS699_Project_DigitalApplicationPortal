from django.db import models

# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  middlename = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  rollno = models.CharField(null= False, max_length=255)
  dept = models.CharField(max_length=255)
  mobno = models.CharField(max_length=255)
  peremail =  models.EmailField()
  iitbemail =  models.EmailField(primary_key=True, max_length=50)
  password =  models.CharField(max_length=255)
  verified =  models.BooleanField()