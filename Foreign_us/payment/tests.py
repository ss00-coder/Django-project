import os

import django
from django.test import TestCase

from member.models import Member
from payment.models import Payment

# Create your tests here.
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

class PaymentTest(TestCase):
    Payment.objects.all().update(pay_status="Y")
    # member = Member.objects.filter(id=1).get()
    # teacher = Member.objects.filter(id=2).get()
    # for i in range(0, 100):
    #     Payment.objects.create(
    #         pay_status='Y' if i % 2 == 0 else 'N',
    #         lesson_type='Y' if i % 3 == 0 else 'N',
    #         member=member,
    #         teacher=teacher
    #     )
    pass