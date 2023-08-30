import os
from itertools import count

import django
from django.db.models import Count
from django.test import TestCase

from payment.models import Payment

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

class AdminTest(TestCase):
     print(Payment.objects.values("teacher_id").annotate(count=Count("teacher_id")).order_by('-count').values('count', 'teacher_id'))