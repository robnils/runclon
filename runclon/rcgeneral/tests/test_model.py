from django.test import TestCase
from rcgeneral.models import Registration


class TestRegistration(TestCase):

    # def setUp(self):
    #     Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
    #                      club="Her Majesty's Secret Service",
    #                      email="james.bond@mi6.co.uk", number="+007")
    #
    #     Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
    #                      club="Treadstone",
    #                      email="jason.bourne@cia.gov", number="+001")
    #
    # def tearDown(self):
    #     Registration.truncate()

    def test_get_all_registrations(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40", club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        regdict = Registration.get_all_registrations_as_dict(exclude=['id', 'updated'])
        self.assertEquals(regdict[0], {
            'bib': "007",
            'first_name': 'James',
            'last_name': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': Registration.PENDING,
        })

        self.assertEquals(regdict[1], {
            'bib': "001",
            'first_name': 'Jason',
            'last_name': 'Bourne',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Treadstone",
            "email": "jason.bourne@cia.gov",
            'number': "+001",
            'status': Registration.PENDING,
        })

    def test_truncate(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
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
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
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
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                     club="Treadstone",
                     email="jason.bourne@cia.gov", number="+001")

        # Assert object creation
        regdict = Registration.get_registration_as_dict(bib="007")
        self.assertEquals(regdict, {
            'bib': "007",
            'first_name': 'James',
            'last_name': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': Registration.PENDING,
        })

    def test_register(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        # Change status
        Registration.register(bib="007")
        regobj = Registration.get_registration_as_obj(bib="007")
        self.assertEquals(regobj.status, Registration.REGISTERED)

    def test_correct_number_of_search_results(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        Registration.add(bib="999", first_name="James", last_name="Bont", gender="Male", age_category="M40",
                         club="Welsh Police",
                         email="james.band@wales.waleland", number="+999")

        registered, not_registered = Registration.search_by_last_name("Bo")
        self.assertEquals(len(registered), 0)
        self.assertEquals(len(not_registered), 3)

        registered, not_registered = Registration.search_by_last_name("Bon")
        self.assertEquals(len(registered), 0)
        self.assertEquals(len(not_registered), 2)

        registered, not_registered = Registration.search_by_last_name("Bont")
        self.assertEquals(len(registered), 0)
        self.assertEquals(len(not_registered), 1)

    def test_search_results_are_correct(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        Registration.add(bib="999", first_name="James", last_name="Bont", gender="Male", age_category="M40",
                         club="Welsh Police",
                         email="james.band@wales.waleland", number="+999")

        Registration.add(bib="002", first_name="Robert", last_name="Hilliard", gender="Male", age_category="MS",
                         club="World Police",
                         email="robert.hilliard@everything.com", number="+001")

        # Register Bont
        Registration.register("007")

        registered, not_registered = Registration.search_by_last_name("Bo")
        self.assertEquals(len(registered), 1)
        self.assertEquals(len(not_registered), 2)

        self.assertEquals(registered[0], {
            'bib': "007",
            'first_name': 'James',
            'last_name': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': Registration.REGISTERED,
            'id': 1,
        })

        self.assertEquals(not_registered[0], {
            'bib': "999",
            'first_name': 'James',
            'last_name': 'Bont',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Welsh Police",
            "email": "james.band@wales.waleland",
            'number': "+999",
            'status': Registration.PENDING,
            'id': 3,
        })

        self.assertEquals(not_registered[1], {
            'bib': "001",
            'first_name': 'Jason',
            'last_name': 'Bourne',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Treadstone",
            "email": "jason.bourne@cia.gov",
            'number': "+001",
            'status': Registration.PENDING,
            'id': 2,
        })

    def test_search_case_insensitive(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")

        registered, not_registered = Registration.search_by_last_name("bON")
        self.assertEquals(len(registered), 0)
        self.assertEquals(len(not_registered), 1)
        self.assertEquals(not_registered[0], {
            'bib': "007",
            'first_name': 'James',
            'last_name': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': Registration.PENDING,
            'id': 1,
        })

    def test_fetch_statistics_works(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        Registration.add(bib="001", first_name="Jason", last_name="Bourne", gender="Male", age_category="M40",
                         club="Treadstone",
                         email="jason.bourne@cia.gov", number="+001")
        Registration.register('001')

        stats = Registration.fetch_statistics()
        self.assertEquals(stats,{
            'total_participants': 2,
            'number_registered': 1,
            'number_not_registered':1,
            'latest_update': None,
        })

    def test_add_non_unique_entries(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")

        with self.assertRaises(ValueError) as err:
            Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                             club="Her Majesty's Secret Service",
                             email="james.bond@mi6.co.uk", number="+007")

    def test_search_by_bib(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")
        results = Registration.search_by_bib('007')
        self.assertEquals(results[0], {
            'bib': "007",
            'first_name': 'James',
            'last_name': 'Bond',
            'gender': 'Male',
            'age_category': 'M40',
            "club": "Her Majesty's Secret Service",
            "email": "james.bond@mi6.co.uk",
            'number': "+007",
            'status': Registration.PENDING,
            'id': 1,
        })

    def test_is_unique_true(self):
        result = Registration.is_unique('007')
        self.assertTrue(result)

    def test_is_unique_false(self):
        Registration.add(bib="007", first_name="James", last_name="Bond", gender="Male", age_category="M40",
                         club="Her Majesty's Secret Service",
                         email="james.bond@mi6.co.uk", number="+007")
        result = Registration.is_unique('007')
        self.assertFalse(result)
