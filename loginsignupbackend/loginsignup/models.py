from django.db import models

class loginsignup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dlnum = models.CharField(max_length=50)
    permitnum = models.CharField(max_length=50)

    def __str__(self):
        return self.name

     
