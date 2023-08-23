import os
import django
from _multiprocessing import send
from django.db.models import Q, Count
from django.test import TestCase

from Foreign_us.models import Message
from event.models import Event, EventLike
from helpers.models import HelpersLike, Helpers
from lesson.models import Lesson, LessonLike
from member.models import Member
from message.models import ReceiveMessage, SendMessage
from review.models import Review

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
    #   Helpers.objects.bulk_create([
    #     Helpers(post_title='후기 제목1', post_content='후기 내용이에요1', post_status='N', member_id=1),
    #     Helpers(post_title='후기 제목2', post_content='후기 내용이에요2', post_status='Y',member_id=2),
    #     Helpers(post_title='후기 제목3', post_content='후기 내용이에요3', post_status='Y',member_id=3),
    #     Helpers(post_title='후기 제목4', post_content='후기 내용이에요4', post_status='Y',member_id=3),
    #     Helpers(post_title='후기 제목5', post_content='후기 내용이에요5', post_status='N',member_id=16),
    #     Helpers(post_title='후기 제목6', post_content='후기 내용이에요6', post_status='Y',member_id=5),
    #     Helpers(post_title='후기 제목7', post_content='후기 내용이에요7', post_status='Y',member_id=1),
    #     Helpers(post_title='후기 제목8', post_content='후기 내용이에요8', post_status='N',member_id=4),
    #     Helpers(post_title='후기 제목9', post_content='후기 내용이에요9', post_status='Y',member_id=5),
    #     Helpers(post_title='후기 제목10', post_content='후기 내용이에요10', post_status='N',member_id=12),
    #     Helpers(post_title='후기 제목11', post_content='후기 내용이에요11', post_status='N',member_id=3),
    #     Helpers(post_title='후기 제목12', post_content='후기 내용이에요12', post_status='Y',member_id=1),
    #     Helpers(post_title='후기 제목1', post_content='후기 내용이에요1', post_status='N', member_id=1),
    #     Helpers(post_title='후기 제목2', post_content='후기 내용이에요2', post_status='Y',member_id=2),
    #     Helpers(post_title='후기 제목3', post_content='후기 내용이에요3', post_status='Y',member_id=3),
    #     Helpers(post_title='후기 제목4', post_content='후기 내용이에요4', post_status='Y',member_id=3),
    #     Helpers(post_title='후기 제목5', post_content='후기 내용이에요5', post_status='N',member_id=16),
    #     Helpers(post_title='후기 제목6', post_content='후기 내용이에요6', post_status='Y',member_id=5),
    #     Helpers(post_title='후기 제목7', post_content='후기 내용이에요7', post_status='Y',member_id=1),
    #     Helpers(post_title='후기 제목8', post_content='후기 내용이에요8', post_status='N',member_id=4),
    #     Helpers(post_title='후기 제목9', post_content='후기 내용이에요9', post_status='Y',member_id=5),
    #     Helpers(post_title='후기 제목10', post_content='후기 내용이에요10', post_status='N',member_id=12),
    #     Helpers(post_title='후기 제목11', post_content='후기 내용이에요11', post_status='N',member_id=3),
    #     Helpers(post_title='후기 제목12', post_content='후기 내용이에요12', post_status='Y',member_id=1),
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
    # status = "N"
    # keyword = "이벤트"
    # events = Event.objects.filter(post_status=status).filter(
    #     Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').values('post_status')
    # print(events)

    # Event.objects.bulk_create([
    #     Event(post_title='이벤트15', post_content='이벤트에요10', post_status='Y', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트16', post_content='이벤트에요20', post_status='Y', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트17', post_content='이벤트에요30', post_status='Y', member_id=3, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트18', post_content='이벤트에요40', post_status='N', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트19', post_content='이벤트에요50', post_status='Y', member_id=16, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트20', post_content='이벤트에요60', post_status='N', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트21', post_content='이벤트에요70', post_status='Y', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트22', post_content='이벤트에요80', post_status='Y', member_id=4, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트23', post_content='이벤트에요90', post_status='N', member_id=5, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트10', post_content='이벤트에요100', post_status='Y', member_id=12, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트11', post_content='이벤트에요110', post_status='N', member_id=3, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #     Event(post_title='이벤트12', post_content='이벤트에요120', post_status='Y', member_id=1, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    # ])


class EventLike(TestCase):
    pass
    # EventLike.objects.bulk_create([
    #     EventLike(member_id=1, event_id=36),
    #     EventLike(member_id=1, event_id=34),
    #     EventLike(member_id=1, event_id=25),
    #     EventLike(member_id=1, event_id=30),
    #     EventLike(member_id=1, event_id=33),
    #     EventLike(member_id=2, event_id=27),
    #     EventLike(member_id=2, event_id=22),
    #     EventLike(member_id=2, event_id=26),
    #     EventLike(member_id=2, event_id=15),
    #     EventLike(member_id=2, event_id=13),
    #     EventLike(member_id=2, event_id=19),
    #     EventLike(member_id=1, event_id=18),
    #     EventLike(member_id=1, event_id=35),
    #     EventLike(member_id=1, event_id=30),
    #     EventLike(member_id=1, event_id=28),
    #     EventLike(member_id=1, event_id=19),
    #     EventLike(member_id=1, event_id=35),
    #     EventLike(member_id=1, event_id=33)
    # ])


class SendMessage(TestCase):
    pass
    # SendMessage.objects.bulk_create([
    #     SendMessage(message_title='쪽지 제목1', message_content='쪽지 내용1', message_status='N', receive_member_id=1, member_id=3),
    #     SendMessage(message_title='쪽지 제목2', message_content='쪽지 내용2', message_status='N', receive_member_id=1, member_id=2),
    #     SendMessage(message_title='쪽지 제목3', message_content='쪽지 내용3', message_status='N', receive_member_id=1, member_id=1),
    #     SendMessage(message_title='쪽지 제목4', message_content='쪽지 내용4', message_status='N', receive_member_id=1, member_id=1),
    #     SendMessage(message_title='쪽지 제목5', message_content='쪽지 내용5', message_status='N', receive_member_id=1, member_id=5),
    #     SendMessage(message_title='쪽지 제목6', message_content='쪽지 내용6', message_status='N', receive_member_id=1, member_id=4),
    #     SendMessage(message_title='쪽지 제목7', message_content='쪽지 내용7', message_status='N', receive_member_id=1, member_id=2),
    #     SendMessage(message_title='쪽지 제목8', message_content='쪽지 내용8', message_status='N', receive_member_id=1, member_id=2),
    #     SendMessage(message_title='쪽지 제목9', message_content='쪽지 내용9', message_status='N', receive_member_id=1, member_id=3),
    #     SendMessage(message_title='쪽지 제목10', message_content='쪽지 내용10', message_status='N', receive_member_id=1, member_id=2),
    #     SendMessage(message_title='쪽지 제목11', message_content='쪽지 내용11', message_status='N', receive_member_id=1, member_id=4)
    # ])


class ReceiveMessage(TestCase):
    pass
    # ReceiveMessage.objects.bulk_create([
    #     ReceiveMessage(message_title='쪽지 제목1', message_content='쪽지 내용1', message_status='N', send_member_id=3, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목2', message_content='쪽지 내용2', message_status='N', send_member_id=2, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목3', message_content='쪽지 내용3', message_status='N', send_member_id=1,  member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목4', message_content='쪽지 내용4', message_status='N', send_member_id=4, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목5', message_content='쪽지 내용5', message_status='N', send_member_id=3, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목6', message_content='쪽지 내용6', message_status='N', send_member_id=2, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목7', message_content='쪽지 내용7', message_status='N', send_member_id=1, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목8', message_content='쪽지 내용8', message_status='N', send_member_id=2, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목9', message_content='쪽지 내용9', message_status='N', send_member_id=4, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목10', message_content='쪽지 내용10', message_status='N', send_member_id=1, member_id=1),
    #     ReceiveMessage(message_title='쪽지 제목11', message_content='쪽지 내용11', message_status='N', send_member_id=3, member_id=1)
    # ])

class Review(TestCase):
    pass
    #   Review.objects.bulk_create([
    #     Review(post_title='후기 제목1', post_content='후기 내용이에요1', post_status='N', member_id=1, reviewed_member_id=2),
    #     Review(post_title='후기 제목2', post_content='후기 내용이에요2', post_status='Y',member_id=2, reviewed_member_id=4),
    #     Review(post_title='후기 제목3', post_content='후기 내용이에요3', post_status='Y',member_id=3, reviewed_member_id=5),
    #     Review(post_title='후기 제목4', post_content='후기 내용이에요4', post_status='Y',member_id=3, reviewed_member_id=5),
    #     Review(post_title='후기 제목5', post_content='후기 내용이에요5', post_status='N',member_id=16, reviewed_member_id=5),
    #     Review(post_title='후기 제목6', post_content='후기 내용이에요6', post_status='Y',member_id=5, reviewed_member_id=5),
    #     Review(post_title='후기 제목7', post_content='후기 내용이에요7', post_status='Y',member_id=1, reviewed_member_id=5),
    #     Review(post_title='후기 제목8', post_content='후기 내용이에요8', post_status='N',member_id=4, reviewed_member_id=3),
    #     Review(post_title='후기 제목9', post_content='후기 내용이에요9', post_status='Y',member_id=5, reviewed_member_id=5),
    #     Review(post_title='후기 제목10', post_content='후기 내용이에요10', post_status='N',member_id=12, reviewed_member_id=5),
    #     Review(post_title='후기 제목11', post_content='후기 내용이에요11', post_status='N',member_id=3, reviewed_member_id=5),
    #     Review(post_title='후기 제목12', post_content='후기 내용이에요12', post_status='Y',member_id=1, reviewed_member_id=5),
    #     Review(post_title='후기 제목1', post_content='후기 내용이에요1', post_status='N', member_id=1, reviewed_member_id=3),
    #     Review(post_title='후기 제목2', post_content='후기 내용이에요2', post_status='Y',member_id=2, reviewed_member_id=5),
    #     Review(post_title='후기 제목3', post_content='후기 내용이에요3', post_status='Y',member_id=3, reviewed_member_id=1),
    #     Review(post_title='후기 제목4', post_content='후기 내용이에요4', post_status='Y',member_id=3, reviewed_member_id=5),
    #     Review(post_title='후기 제목5', post_content='후기 내용이에요5', post_status='N',member_id=16, reviewed_member_id=3),
    #     Review(post_title='후기 제목6', post_content='후기 내용이에요6', post_status='Y',member_id=5, reviewed_member_id=5),
    #     Review(post_title='후기 제목7', post_content='후기 내용이에요7', post_status='Y',member_id=1, reviewed_member_id=5),
    #     Review(post_title='후기 제목8', post_content='후기 내용이에요8', post_status='N',member_id=4, reviewed_member_id=1),
    #     Review(post_title='후기 제목9', post_content='후기 내용이에요9', post_status='Y',member_id=5, reviewed_member_id=5),
    #     Review(post_title='후기 제목10', post_content='후기 내용이에요10', post_status='N',member_id=12, reviewed_member_id=5),
    #     Review(post_title='후기 제목11', post_content='후기 내용이에요11', post_status='N',member_id=3, reviewed_member_id=1),
    #     Review(post_title='후기 제목12', post_content='후기 내용이에요12', post_status='Y',member_id=1, reviewed_member_id=5),
    # ])
