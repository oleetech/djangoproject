from django.db import models

# Create your models here.

class Citizen (models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)


class Nid(models.Model):
    citizen = models.OneToOneField(Citizen,on_delete=models.CASCADE,related_name='nid')
    nid_number = models.IntegerField()
    issue_date = models.DateField()
    expire_date = models.DateField()