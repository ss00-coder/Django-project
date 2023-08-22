import os

import django
from django.test import TestCase

from member.models import Member
from review.models import Review

# Create your tests here.
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

class ReviewTest(TestCase):
    member = Member.objects.get(id=1)
    teacher = Member.objects.get(id=2)
    Review.objects.create(
        member=member,
        reviewed_member=teacher,
        post_title="리뷰 제목 테스트",
        post_content="리뷰 내용 테스트"
    )