from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    bib = models.IntegerField(max_length=10, default='')
    first_name = models.CharField(max_length=40, default='')
    surname = models.CharField(max_length=40, default='')
    gender = models.CharField(max_length=10, default='')
    age_category = models.CharField(max_length=10, default='')
    club = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=10, default='')
    number = models.CharField(max_length=10, default='')