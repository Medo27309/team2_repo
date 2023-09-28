from django.db import models
class user(models.Model):
    name=models.CharField(primary_key= True, max_length=30)
    mail=models.TextField(max_length=80, null=False, default=None)
    password=models.TextField(max_length=28, null=False)
    dob=models.DateField()
# Create your models here.
