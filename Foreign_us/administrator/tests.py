import os

import django
from django.db.models import Q
from django.test import TestCase

from lesson.models import Lesson
from member.models import Member
from message.models import ReceiveMessage, SendMessage
from notice.models import Notice, NoticeFile
from review.models import Review, ReviewFile

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

class AdminTest(TestCase):
    # for i in range(13):
    #     Lesson.objects.create(
    #         post_title=f"석님의 레슨{i+1}",
    #         post_content=f"석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아 석님의 레슨 너무 재밌다아",
    #         member_id=1
    #     )

    # for i in range(34, 47):
    #     Review.objects.create(
    #         post_title=f"석이님 최고{i}",
    #         post_content="최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고최고",
    #         post_status="Y",
    #         member_id=i % 5 + 1,
    #         reviewed_member_id=1
    #     )

    # ReviewFile.objects.create(
    #     review_id=50,
    #     image="notice/2023/08/21/dogs.jpg"
    # )

    # for i in range(0, 100):
    #     ReceiveMessage.objects.create(
    #         message_title=f"문의사항 제목{i+1}",
    #         message_content=f"문의사항 내용{i+1}",
    #         send_member=Member.objects.get(id=1),
    #         member=Member.objects.get(id=19)
    #     )

    # SendMessage.objects.create(
    #     message_title="문의사항 답변 제목",
    #     message_content="문의사항 답변 내용",
    #     message=ReceiveMessage.objects.get(id=154),
    #     member=Member.objects.get(id=19),
    #     receive_member=Member.objects.get(id=1)
    # )

    # Member.objects.create(
    #     member_email='admin@gmail.com',
    #     member_nickname='관리자 임희수',
    #     member_type='A'
    # )

    # member = Member.objects.filter(member_type='A').get()
    # for i in range(0, 100):
    #     Notice.objects.create(
    #         post_title=f'공지사항 제목{i+1}',
    #         post_content=f'공지사항 내용{i+1}',
    #         member=member
    #     )

    # Notice.objects.create(
    #     post_title=f'공지사항 제목',
    #     post_content=f'공지사항 내용',
    #     member=Member.objects.filter(member_type='A').get()
    # )

    # notice = Notice.objects.filter(id=316).get()
    # print(notice.post_content)
    # notice.post_title="수정된 공지사항 제목"
    # notice.save()
    # post = Notice.objects.filter(id=314).get()
    # prevFiles = ['notice/2023/08/18/cute-girl_5ulLRGB.jpg']
    # NoticeFile.objects.exclude(image__in=prevFiles).delete()
    # NoticeFile.objects.filter(Q(notice=post) & ~Q(image__in=prevFiles)).delete()
    pass