from django.db import models

# Create your models here.
class product(models.Model):
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=20)
