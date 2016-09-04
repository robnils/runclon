from django.test import TestCase
from rcgeneral.models import Registration


class TestRegistration(TestCase):

    def test_get_all_registrations(self):
        Registration.add(bib="007", first_name="James", surname="Bond", gender="Male", age_category="M40", club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", surname="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        regdict = Registration.get_all_registrations_as_dict(exclude=['id', 'updated'])
        self.assertEquals(regdict[0], {
            'bib': "007",
            'first_name': 'James',
            'surname': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': "pending",
        })

        self.assertEquals(regdict[1], {
            'bib': "001",
            'first_name': 'Jason',
            'surname': 'Bourne',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Treadstone",
            "email": "jason.bourne@cia.gov",
            'number': "+001",
            'status': "pending",
        })

    def test_truncate(self):
        Registration.add(bib="007", first_name="James", surname="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        # Assert object creation
        regobj = Registration.get_all_registrations_as_obj()
        self.assertEquals(len(regobj), 1, "Should have only one Registration")

        # Delete and assert
        Registration.truncate()
        regobj = Registration.get_all_registrations_as_obj()
        self.assertEquals(len(regobj), 0, "Registration table should be empty now")


    def test_delete_registration(self):
        Registration.add(bib="007", first_name="James", surname="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="007")

        Registration.add(bib="001", first_name="Jason", surname="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        # Assert object creation
        regobj = Registration.get_all_registrations_as_obj()
        self.assertEquals(len(regobj), 2, "Missing registration")

        # Delete bourne (bond comes first...)
        Registration.delete_registration(bib='001')
        regobj = Registration.get_all_registrations_as_obj()
        self.assertEquals(len(regobj), 1, "Registration bourne wasn't deleted!")

    def test_get_registration(self):
        Registration.add(bib="007", first_name="James", surname="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", surname="Bourne", gender="Male", age_category="M40",
                     club="Treadstone",
                     email="jason.bourne@cia.gov", number="+001")

        # Assert object creation
        regdict = Registration.get_registration_as_dict(bib="007")
        self.assertEquals(regdict, {
            'bib': "007",
            'first_name': 'James',
            'surname': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': "pending",
        })



