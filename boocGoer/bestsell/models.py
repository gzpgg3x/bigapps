from django.db import models
from datetime import datetime

class Shout(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    booklist = models.CharField(max_length=50,blank=True)
    bldate = models.TextField(blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=80,blank=True)
    isbn = models.CharField(max_length=15,blank=True)

    author = models.CharField(max_length=80,blank=True)
    publisher = models.CharField(max_length=15,blank=True)
    description = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.booklist, self.bldate[:20])