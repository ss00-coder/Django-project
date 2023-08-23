import os

import django
from django.test import TestCase

from member.models import MemberFile, Member

# Create your tests here.
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

class ProfileTest(TestCase):
    MemberFile.objects.create(
        image="notice/2023/08/21/dogs.jpg",
        file_type='B',
        member=Member.objects.get(id=19)
    )
    pass