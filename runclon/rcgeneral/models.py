from __future__ import unicode_literals
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
    surname = models.CharField(max_length=60, default='')
    gender = models.CharField(max_length=10, default='')
    age_category = models.CharField(max_length=10, default='')
    club = models.CharField(max_length=80, default='')
    email = models.CharField(max_length=180, default='')
    number = models.CharField(max_length=40, default='')
    #tshirt = models.CharField(max_length=5, default='') # TODO implement
    status = models.CharField(max_length=50, default=PENDING)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{},{},{}".format(self.bib, self.first_name, self.surname)

    @staticmethod
    def add(bib='', first_name='', surname='', gender='', age_category='', club='', email='', number=''):
        cust = Registration.objects.create(bib=bib, first_name=first_name, surname=surname, gender=gender, age_category=age_category,
                                           club=club, email=email, number=number, status=Registration.PENDING)

        cust.save()

    @staticmethod
    def get_all_registrations_as_obj():
        return Registration.objects.all()

    @staticmethod
    def get_all_registrations_as_dict(exclude=['updated', 'id']):
        # Return a list of dictionarys representing each object
        return [Registration._serial_model(reg, exclude) for reg in Registration.get_all_registrations_as_obj()]

    @staticmethod
    def _update_registration(bib, status):
        regobj = Registration.get_registration_as_obj(bib=bib)
        regobj.status = status
        regobj.save()

    @staticmethod
    def register(bib):
        Registration._update_registration(bib=bib, status=Registration.REGISTERED)

    @staticmethod
    def get_registration_as_obj(bib):
        return Registration.objects.get(bib=bib)

    @staticmethod
    def get_registration_as_dict(bib):
        regobj = Registration.get_registration_as_obj(bib)
        return Registration._serial_model(regobj, exclude=['id'])

    @staticmethod
    def _serial_model(model_obj, exclude=[]):
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
    def search_by_last_name(text):
        results = Registration.get_all_registrations_as_obj().filter(surname__contains=text)
        not_registered = results.filter(status=Registration.PENDING).order_by('surname')
        registered = results.filter(status=Registration.REGISTERED).order_by('surname')
        return Registration._obj_to_dict(registered), Registration._obj_to_dict(not_registered)

    @staticmethod
    def _obj_to_dict(list_of_obj):
        return [Registration._serial_model(obj) for obj in list_of_obj]
