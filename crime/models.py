from django.db import models

# Create your models here.
class Crime(models.Model):
    title = models.CharField(max_length=100, blank=False)
    refno=models.CharField(max_length=100, blank=False, null=False)
    section = models.CharField(max_length=100, blank=False)
    subsection = models.CharField(max_length=100, blank=False)
    acts = models.CharField(max_length=100, blank=False)
    charges = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.refno
    
