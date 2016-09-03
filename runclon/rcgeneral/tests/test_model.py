from django.test import TestCase
from rcgeneral.models import Registration


class TestRegistration(TestCase):

    def test_get_registrations(self):
        Registration.add(bib="007", first_name="James", surname="Bond", gender="Male", age_category="M40", club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="007")

        regdict = Registration.get_registrations_as_dict()[0]
        self.assertEquals(regdict, {
            'bib': "007",
            'first_name': 'James',
            'surname': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "007",
        })

