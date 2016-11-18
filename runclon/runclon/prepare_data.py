import csv
import functools

import os
import django
import names
import random

# Initialise django
os.environ['DJANGO_SETTINGS_MODULE'] = 'runclon.settings'
django.setup()

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

if __name__ == "__main__":
    pass


