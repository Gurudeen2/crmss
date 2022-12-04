from django.db import models
from crime.models import Crime

# Create your models here.

class Criminal(models.Model):
    fullname = models.CharField(max_length=50, blank=False, null=False)
    nin = models.DecimalField(decimal_places=0, max_digits=20)
    crime = models.ForeignKey(Crime, on_delete=models.DO_NOTHING, null=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    charge = models.TextField(blank=True)

    def __str__(self):
        self.fullname