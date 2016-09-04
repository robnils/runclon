from __future__ import unicode_literals

import datetime

from django.db import models


# Create your models here.
from django.forms import model_to_dict


class Registration(models.Model):
    bib = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=60, default='')
    surname = models.CharField(max_length=60, default='')
    gender = models.CharField(max_length=10, default='')
    age_category = models.CharField(max_length=10, default='')
    club = models.CharField(max_length=80, default='')
    email = models.CharField(max_length=180, default='')
    number = models.CharField(max_length=40, default='')
    status = models.CharField(max_length=50, default='pending')
    # pending, registered, (started), finished
    updated = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def add(bib='', first_name='', surname='', gender='', age_category='', club='', email='', number=''):
        cust = Registration.objects.create(bib=bib, first_name=first_name, surname=surname, gender=gender, age_category=age_category,
                                           club=club, email=email, number=number, status='pending')

        cust.save()

    @staticmethod
    def get_registrations_as_obj():
        return Registration.objects.all()

    @staticmethod
    def get_registrations_as_dict(exclude=['status', 'updated', 'id']):
        # Return a list of dictionarys representing each object
        return [Registration.serial_model(reg, exclude) for reg in Registration.get_registrations_as_obj()]

    @staticmethod
    def serial_model(model_obj, exclude=[]):
        opts = model_obj._meta.fields
        modeldict = model_to_dict(model_obj, exclude=exclude)
        print modeldict
        for m in opts:
            if m.is_relation:
                foreignkey = getattr(model_obj, m.name)
                if foreignkey:
                    try:
                        modeldict[m.name] = Registration.serial_model(foreignkey)
                    except:
                        pass
        return modeldict