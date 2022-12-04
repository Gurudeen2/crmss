from django.db import models

# Create your models here.

class Account(models.Model):
    userid = models.CharField(primary_key=True, max_length=100 )
    firstname = models.CharField(max_length=30, blank=False, null=False)
    middlename = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    passowrd = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return self.userid



