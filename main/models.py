from django.db import models

class LinksMapper(models.Model):
    link= models.CharField(max_length=2000)
    short= models.CharField(max_length=10,unique=True)
   