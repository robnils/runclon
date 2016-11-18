from __future__ import unicode_literals
import functools
import random

import names
from django.core.management.base import BaseCommand

from rcgeneral.models import Registration


class Command(BaseCommand):
    help = 'Creates an initital state of the system for local development'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)
        parser.add_argument('rprob', type=float)

    def random_phone_number(self, num_digits):
        rand = functools.partial(random.randint, 0, num_digits)
        number = '+'
        for idx in range(0, num_digits):
            number += str(rand())
        return number

    def generate_random_registration_data(self, max_participants, registered_parameter=0.0):
        assert 0 <= registered_parameter <= 1, 'registered_parameter {} given outside range!'.format(registered_parameter)
        INT_TO_GENDER_MAP = {
            0: 'male',
            1: 'female',
        }
        AGE_CATEGORY_MAP = {
            0: '10+',
            1: '18+',
            2: '30+',
            3: '40+',
            4: '60+',
        }

        # Deliberately longer as it's more likely that a runner isn't part of a club
        CLUB_MAP = {
            0: '',
            1: 'cork',
            2: 'a club',
            3: 'super runners',
            4: 'run4life',
            5: '',
            6: '',
            7: '',
        }

        TSHIRT_SIZE_MAP = {
            0: 'XXS',
            1: 'XS',
            2: 'S',
            3: 'M',
            4: 'L',
            5: 'XL',
            6: 'XXL',
            7: 'XXXL',
        }

        assert max_participants > 1, 'max_participants must be an integer greater than 1!'

        for idx in range(0, int(max_participants)):
            bib = str(idx)
            gender_rand = random.randrange(0, 2)
            gender = INT_TO_GENDER_MAP[gender_rand]

            first_name = names.get_first_name(gender=gender)
            last_name = names.get_last_name()

            age_idx = random.randrange(0, len(AGE_CATEGORY_MAP))
            age_category = AGE_CATEGORY_MAP[age_idx]

            club_idx = random.randrange(0, len(CLUB_MAP))
            club = CLUB_MAP[club_idx]

            email = '{}.{}@TestyMcTestFace.test'.format(first_name, last_name)
            number = self.random_phone_number(11)

            tshirt_size_idx = random.randrange(0, len(TSHIRT_SIZE_MAP))
            tshirt_size = TSHIRT_SIZE_MAP[tshirt_size_idx]

            try:
                cust = Registration.add(bib, first_name, last_name, gender, age_category, club, email, number, tshirt_size)
                print "Added {}".format(cust)
            except Exception as exp:
                self.stderr.write(exp.message)

            if registered_parameter > 0.0:
                to_register = random.uniform(0.0, 1.0) >= (1.0 - registered_parameter)
                if to_register:
                    try:
                        Registration.register(bib)
                        self.stdout.write('Registered {}'.format(bib))
                    except Exception as exp:
                        self.stderr.write(exp.message)

        self.stdout.write("Added {} registrations to table".format(idx + 1))

    def handle(self, *args, **options):
        number = options['number']
        rprob = options['rprob']
        try:
            # Try clear db if defined, otherwise, move on
            try:
                Registration.truncate()
            except:
                pass

            self.generate_random_registration_data(number, rprob)
        except Exception as exp:
            self.stderr.write(exp.message)
