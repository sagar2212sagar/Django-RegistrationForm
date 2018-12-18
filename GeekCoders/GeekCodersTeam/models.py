from django.db import models
import datetime

class login1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=50)
    address1=models.CharField(max_length=500)
    paddress=models.CharField(max_length=500)
    education=models.CharField(max_length=500)
    url=models.CharField(max_length=500)
    hacker=models.CharField(max_length=50)
    linkdin=models.CharField(max_length=50)
    git=models.CharField(max_length=50)
    blog=models.CharField(max_length=500)


    def __str__(self):
        return self.name





