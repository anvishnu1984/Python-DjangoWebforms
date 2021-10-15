from django.db import models
from django.urls import reverse

class  Environment(models.Model):

   name = models.CharField(null=False,blank = False, max_length = 255)

   def get_absolute_url(self):
       return reverse('Environment:Environment_detail', kwargs={'pk' : self.pk})
   def __str__(self):
       return self.name


class TagVersions(models.Model):

    tagnumber = models.CharField(null=False,blank=False, max_length = 255)

    Environment = models.ForeignKey('Environment', null = False, blank = False, on_delete= models.CASCADE, related_name = 'environment')

# Create your models here.
