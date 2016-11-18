# -*- coding: utf-8 -*
from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
from django.forms import model_to_dict

class Registration(models.Model):

    # Statuses
    PENDING = "PENDING"
    REGISTERED = "REGISTERED"
    COMPLETED = "COMPLETED"

    bib = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    gender = models.CharField(max_length=10, default='')
    age_category = models.CharField(max_length=10, default='')
    club = models.CharField(max_length=80, default='')
    email = models.CharField(max_length=180, default='')
    number = models.CharField(max_length=40, default='')
    tshirt_size = models.CharField(max_length=10, default='')
    registered_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default=PENDING)
    #updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{},{},{},{}".format(self.bib, self.first_name, self.last_name, self.tshirt_size)

    @staticmethod
    def add(bib='', first_name='', last_name='', gender='', age_category='', club='', email='', number='', tshirt_size=''):
        if not Registration.is_unique(bib):
            raise ValueError('Duplicate entry! {bib} {first_name} {last_name}'.format(bib=bib,first_name=first_name, last_name=last_name))

        cust = Registration.objects.create(bib=bib, first_name=first_name, last_name=last_name, gender=gender, age_category=age_category,
                                           club=club, email=email, number=number, status=Registration.PENDING, tshirt_size=tshirt_size)

        cust.save()
        return cust

    @staticmethod
    def get_all_registrations_as_obj():
        return Registration.objects.all()

    @staticmethod
    def get_all_registrations_as_dict(exclude=None):
        if not exclude:
            exclude = ['updated', 'id']
        # Return a list of dictionaries representing each object
        return [Registration._serial_model(reg, exclude) for reg in Registration.get_all_registrations_as_obj()]

    @staticmethod
    def _update_registration(bib, status):
        regobj = Registration.get_registration_as_obj(bib=bib)
        regobj.status = status
        regobj.registered_time = datetime.datetime.now()
        regobj.save()

    @staticmethod
    def register(bib):
        # TODO add proper validation
        if not bib:
            raise Exception("Bib number cannot be None!")
        Registration._update_registration(bib=bib, status=Registration.REGISTERED)

    @staticmethod
    def get_registration_as_obj(bib):
        return Registration.objects.get(bib=bib)

    @staticmethod
    def get_registration_as_dict(bib):
        regobj = Registration.get_registration_as_obj(bib)
        return Registration._serial_model(regobj, exclude=['id'])

    @staticmethod
    def _serial_model(model_obj, exclude=None):
        if not exclude:
            exclude = []

        opts = model_obj._meta.fields
        modeldict = model_to_dict(model_obj, exclude=exclude)
        for m in opts:
            if m.is_relation:
                foreignkey = getattr(model_obj, m.name)
                if foreignkey:
                    try:
                        modeldict[m.name] = Registration._serial_model(foreignkey)
                    except:
                        pass
        return modeldict

    @staticmethod
    def truncate():
        return Registration.get_all_registrations_as_obj().delete()

    @staticmethod
    def delete_registration(bib):
        return Registration.get_registration_as_obj(bib).delete()

    @staticmethod
    def is_unique(text):
        return Registration.get_all_registrations_as_obj().filter(bib=text).count() == 0

    @staticmethod
    def search_by_bib(text):
        results = Registration.get_all_registrations_as_obj().filter(bib=text)
        return Registration._obj_to_dict(results)

    @staticmethod
    def search_by_last_name(text):
        results = Registration.get_all_registrations_as_obj().filter(last_name__contains=text)
        not_registered = results.filter(status=Registration.PENDING).order_by('last_name')
        registered = results.filter(status=Registration.REGISTERED).order_by('last_name')
        return Registration._obj_to_dict(registered), Registration._obj_to_dict(not_registered)

    @staticmethod
    def search_by_first_name(text):
        results = Registration.get_all_registrations_as_obj().filter(first_name__contains=text)
        not_registered = results.filter(status=Registration.PENDING).order_by('first_name')
        registered = results.filter(status=Registration.REGISTERED).order_by('first_name')
        return Registration._obj_to_dict(registered), Registration._obj_to_dict(not_registered)

    @staticmethod
    def fetch_statistics():
        registrations = Registration.get_all_registrations_as_obj()
        total_participants = registrations.count()
        number_registered = registrations.filter(status=Registration.REGISTERED).count()
        number_not_registered = registrations.filter(status=Registration.PENDING).count()

        latest_update_list = registrations.filter(status=Registration.REGISTERED).order_by('registered_time')
        if latest_update_list.exists():
            latest_update = latest_update_list.first().registered_time
        else:
            latest_update = None
        percentage_registered = None # TODO implement

        return {
            'total_participants': total_participants,
            'number_registered': number_registered,
            'number_not_registered': number_not_registered,
            'latest_update': latest_update,
        }

    @staticmethod
    def _obj_to_dict(list_of_obj):
        return [Registration._serial_model(obj) for obj in list_of_obj]
