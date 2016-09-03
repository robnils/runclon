from __future__ import unicode_literals

import datetime

from django.db import models


# Create your models here.
class Customer(models.Model):
    bib = models.IntegerField(default='')
    first_name = models.CharField(max_length=40, default='')
    surname = models.CharField(max_length=40, default='')
    gender = models.CharField(max_length=10, default='')
    age_category = models.CharField(max_length=10, default='')
    club = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=10, default='')
    number = models.CharField(max_length=10, default='')
    status = models.CharField(max_length=10, default='pending')
    # pending, registered, (started), finished
    updated = models.TimeField(max_length=10)

    @staticmethod
    def add(bib='', first_name='', surname='', gender='', age_category='', club='', email='', number=''):
        now = datetime.datetime.now()
        cust = Customer.objects.create(bib=bib, first_name=first_name, surname=surname, gender=gender, age_category=age_category,
                                       club=club, email=email, number=number, status='pending', updated=now)

        cust.save()

    def get_customers(self):
        return self.Customer_set.all()


