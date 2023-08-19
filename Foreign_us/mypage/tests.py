import os
import django
from django.db.models import Q, Count
from django.test import TestCase

from event.models import Event, EventLike
from helpers.models import HelpersLike
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
    pass
    # LessonLike.objects.bulk_create([
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=2, lesson_id=47),
    #     LessonLike(member_id=2, lesson_id=47),
    #     LessonLike(member_id=2, lesson_id=47),
    #     LessonLike(member_id=2, lesson_id=47),
    #     LessonLike(member_id=2, lesson_id=46),
    #     LessonLike(member_id=2, lesson_id=46),
    #     LessonLike(member_id=1, lesson_id=46),
    #     LessonLike(member_id=1, lesson_id=46),
    #     LessonLike(member_id=1, lesson_id=46),
    #     LessonLike(member_id=1, lesson_id=46),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48),
    #     LessonLike(member_id=1, lesson_id=48)
    #
    # ])


class Helpers(TestCase):
    pass
    # Helpers.objects.bulk_create([
    #     Helpers(post_title='도움1', post_content='도와주세요1', member_id=1),
    #     Helpers(post_title='도움2', post_content='도와주세요2', member_id=2),
    #     Helpers(post_title='도움3', post_content='도와주세요3', member_id=3),
    #     Helpers(post_title='도움4', post_content='도와주세요4', member_id=3),
    #     Helpers(post_title='도움5', post_content='도와주세요5', member_id=16),
    #     Helpers(post_title='도움6', post_content='도와주세요6', member_id=5),
    #     Helpers(post_title='도움7', post_content='도와주세요7', member_id=1),
    #     Helpers(post_title='도움8', post_content='도와주세요8', member_id=4),
    #     Helpers(post_title='도움9', post_content='도와주세요9', member_id=5),
    #     Helpers(post_title='도움10', post_content='도와주세요10', member_id=12),
    #     Helpers(post_title='도움11', post_content='도와주세요11', member_id=3),
    #     Helpers(post_title='도움12', post_content='도와주세요12', member_id=1),
    # ])


class HelpersLike(TestCase):
    pass
    # HelpersLike.objects.bulk_create([
    #     HelpersLike(member_id=1, helpers_id=5),
    #     HelpersLike(member_id=1, helpers_id=11),
    #     HelpersLike(member_id=1, helpers_id=11),
    #     HelpersLike(member_id=1, helpers_id=2),
    #     HelpersLike(member_id=1, helpers_id=9),
    #     HelpersLike(member_id=2, helpers_id=9),
    #     HelpersLike(member_id=2, helpers_id=3),
    #     HelpersLike(member_id=2, helpers_id=2),
    #     HelpersLike(member_id=2, helpers_id=3),
    #     HelpersLike(member_id=2, helpers_id=1),
    #     HelpersLike(member_id=2, helpers_id=1),
    #     HelpersLike(member_id=1, helpers_id=1),
    #     HelpersLike(member_id=1, helpers_id=4),
    #     HelpersLike(member_id=1, helpers_id=4),
    #     HelpersLike(member_id=1, helpers_id=2),
    #     HelpersLike(member_id=1, helpers_id=1),
    #     HelpersLike(member_id=1, helpers_id=1),
    #     HelpersLike(member_id=1, helpers_id=4)
    # ])

class Event(TestCase):
    pass
    # Event.objects.bulk_create([
    #     Event(post_title='이벤트1', post_content='이벤트에요1', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트2', post_content='이벤트에요2', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트3', post_content='이벤트에요3', member_id=3, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트4', post_content='이벤트에요4', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트5', post_content='이벤트에요5', member_id=16, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트6', post_content='이벤트에요6', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트7', post_content='이벤트에요7', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트8', post_content='이벤트에요8', member_id=4, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트9', post_content='이벤트에요9', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트10', post_content='이벤트에요10', member_id=12, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트11', post_content='이벤트에요11', member_id=3, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트12', post_content='이벤트에요12', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    # ])

class EventLike(TestCase):
    EventLike.objects.bulk_create([
        EventLike(member_id=1, event_id=36),
        EventLike(member_id=1, event_id=34),
        EventLike(member_id=1, event_id=25),
        EventLike(member_id=1, event_id=30),
        EventLike(member_id=1, event_id=33),
        EventLike(member_id=2, event_id=27),
        EventLike(member_id=2, event_id=22),
        EventLike(member_id=2, event_id=26),
        EventLike(member_id=2, event_id=15),
        EventLike(member_id=2, event_id=13),
        EventLike(member_id=2, event_id=19),
        EventLike(member_id=1, event_id=18),
        EventLike(member_id=1, event_id=35),
        EventLike(member_id=1, event_id=30),
        EventLike(member_id=1, event_id=28),
        EventLike(member_id=1, event_id=19),
        EventLike(member_id=1, event_id=35),
        EventLike(member_id=1, event_id=33)
    ])
