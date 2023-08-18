import os
import django
from django.db.models import Q, Count
from django.test import TestCase

from lesson.models import Lesson, LessonLike
from member.models import Member

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()


# class MemberTest(TestCase):
#     # 클래스 내부에 코드를 작성하면, 커밋 된다.
#     # 하지만 메소드 내에서 코드를 작성하면, 롤백 된다.
#
#     # ======================================
#     # bulk_create
#     # ======================================
#
#     Member.objects.bulk_create([
#         Member(member_email='test55@gmail.com', member_nickname='석'),
#         Member(member_email='test95@naver.com', member_nickname='길동'),
#         Member(member_email='test3@naver.com', member_nickname='짱구'),
#         Member(member_email='test4@google.com', member_nickname='철수'),
#         Member(member_email='test5@nate.com', member_nickname='유리'),
#     ])


class Lesson(TestCase):
    pass
    # Lesson.objects.bulk_create([
    #     Lesson(post_title='영어', post_content='영어과외', post_view_count=12, post_status='Y', member_id=1),
    #     Lesson(post_title='스페인어', post_content='일본어과외',post_view_count=142, post_status='Y', member_id=2),
    #     Lesson(post_title='스웨덴어', post_content='중국어과외', post_view_count=24, post_status='N', member_id=3),
    #     Lesson(post_title='독일어', post_content='독일어과외', post_view_count=19, post_status='Y', member_id=4),
    #     Lesson(post_title='영어', post_content='영어과외', post_view_count=124, post_status='N', member_id=5),
    #     Lesson(post_title='히말라야어', post_content='일본어과외', post_view_count=122, post_status='Y', member_id=5),
    #     Lesson(post_title='중국어', post_content='중국어과외', post_view_count=95, post_status='N', member_id=1),
    #     Lesson(post_title='독일어', post_content='독일어과외', post_view_count=42, post_status='Y', member_id=1),
    # ])


class LessonLike(TestCase):
    LessonLike.objects.bulk_create([
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=2, lesson_id=47),
        LessonLike(member_id=2, lesson_id=47),
        LessonLike(member_id=2, lesson_id=47),
        LessonLike(member_id=2, lesson_id=47),
        LessonLike(member_id=2, lesson_id=46),
        LessonLike(member_id=2, lesson_id=46),
        LessonLike(member_id=1, lesson_id=46),
        LessonLike(member_id=1, lesson_id=46),
        LessonLike(member_id=1, lesson_id=46),
        LessonLike(member_id=1, lesson_id=46),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48),
        LessonLike(member_id=1, lesson_id=48)

    ])