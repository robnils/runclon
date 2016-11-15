import csv
import os
import django
import names
import random

# Initialise django
os.environ['DJANGO_SETTINGS_MODULE'] = 'runclon.settings'
django.setup()

from runclon import settings
from rcgeneral.models import Registration

def read_csv(filepath):
    f = open(filepath, 'rb')
    try:
        reader = csv.reader(f)
        return reader
    finally:
        f.close()

def fetch_data_from_file(path):
    #path = os.path.join(os.getcwd(), 'reg.csv')
    print "Importing data from: {}".format(path)
    f = open(path, 'rb')
    try:
        reader = csv.reader(f)
        print "Done!"
        idx = 0
        for row in reader:
            # ['BIB', 'FIRSTNAME', 'FAMILY', 'GEN', 'AGE', 'CLUB', 'EMIAL', 'MOB']
            if idx > 0:

                # create model
                bib = row[0]
                first_name = row[1]
                last_name = row[2]
                gender = row[3]
                age_category = row[4]
                club = row[5]
                email = row[6]
                number = row[7]

                try:
                    Registration.add(bib, first_name, last_name, gender, age_category, club, email, number)
                    print "Added {}".format(" ".join(row))
                except Exception as exp:
                    print exp

            idx += 1

    finally:
        f.close()


def generate_random_registration_data(max_participants):
    int_to_gender_map = {
        0: 'male',
        1: 'female',
    }
    age_category_map = {
        0: '10+',
        1: '18+',
        2: '30+',
        3: '40+',
        4: '60+',
    }

    club_map = {
        0: '',
        1: 'cork',
        2: 'a club',
        3: 'super runners',
        4: 'run4life',
    }

    for idx in range(0, max_participants):
        bib = str(idx)
        gender_rand = random.randrange(0, 2)
        gender = int_to_gender_map[gender_rand]

        first_name = names.get_first_name(gender=gender)
        last_name = names.get_last_name()

        age_idx = random.randrange(0, len(age_category_map))
        age_category = age_category_map[age_idx]

        club_idx = random.randrange(0, len(club_map))
        club = age_category_map[club_idx]

        email = 'test@TestyMcTestFace.test'
        number = '+1234565789123'

        try:
            cust = Registration.add(bib, first_name, last_name, gender, age_category, club, email, number)
            print "Added {}".format(cust)
        except Exception as exp:
            print exp
    print "Added {} registrations to table".format(idx + 1)

if __name__ == "__main__":
    # Try clear db if defined, otherwise, move on

    generate_random_registration_data(2000)

