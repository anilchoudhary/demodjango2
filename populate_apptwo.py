import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo_project.settings')
import django
django.setup()

# fake pop script

import random
from apptwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):

        # create the fake data for that entry
        fn = fakegen.name().split(" ")
        fake_fn = fn[0]
        fake_ln = fn[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(
            first_name=fake_fn, last_name=fake_ln, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
