import os
import django
from _multiprocessing import send
from django.db.models import Q, Count
from django.test import TestCase

from Foreign_us.models import Message
from event.models import Event, EventLike
from helpers.models import HelpersLike, Helpers
from lesson.models import Lesson, LessonLike
from member.models import Member, MemberFile
from message.models import ReceiveMessage, SendMessage
from review.models import Review

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()


class MemberTest(TestCase):
    # 클래스 내부에 코드를 작성하면, 커밋 된다.
    # 하지만 메소드 내에서 코드를 작성하면, 롤백 된다.

    # ======================================
    # bulk_create
    # ======================================

    # Member.objects.bulk_create([
        pass
    #     Member(member_email='test1@gmail.com', member_nickname='지우', member_intro='안녕하세요!',
    #            member_intro_detail='한국에 놀러오게 되어 기뻐요.'),
    #     Member(member_email='test2@gmail.com', member_nickname='하나', member_intro='안녕하세요, 저는 하나입니다.',
    #            member_intro_detail='음악을 좋아하고 새로운 사람들을 만나는 걸 좋아해요.'),
    #     Member(member_email='test3@gmail.com', member_nickname='정우', member_intro='안녕하세요, 정우입니다.',
    #            member_intro_detail='맛있는 음식과 여행을 사랑합니다.'),
    #     Member(member_email='test4@gmail.com', member_nickname='예은', member_intro='안녕하세요! 저는 예은에요.',
    #            member_intro_detail='예술과 문화에 관심이 많아요.'),
    #     Member(member_email='test5@gmail.com', member_nickname='도현', member_intro='안녕하세요, 도현입니다.',
    #            member_intro_detail='스포츠와 영화를 좋아합니다.'),
    #     Member(member_email='test6@gmail.com', member_nickname='미나', member_intro='안녕하세요, 미나에요!',
    #            member_intro_detail='새로운 친구를 만나고 싶어요.'),
    #     Member(member_email='test7@gmail.com', member_nickname='민준', member_intro='안녕하세요, 민준입니다.',
    #            member_intro_detail='자연과 활동을 즐겨요.'),
    #     Member(member_email='test8@gmail.com', member_nickname='서연', member_intro='안녕하세요, 서연이에요.',
    #            member_intro_detail='다양한 문화를 경험하고 싶어요.'),
    #     Member(member_email='test9@gmail.com', member_nickname='동하', member_intro='안녕하세요, 동하입니다.',
    #            member_intro_detail='음악과 음식을 사랑합니다.'),
    #     Member(member_email='test10@gmail.com', member_nickname='하린', member_intro='안녕하세요, 저는 하린입니다.',
    #            member_intro_detail='여행을 좋아하고 새로운 경험을 찾고 있어요.'),
    #     Member(member_email='test11@gmail.com', member_nickname='승우', member_intro='안녕하세요, 승우입니다.',
    #            member_intro_detail='스포츠와 모험을 좋아합니다.'),
    #     Member(member_email='test12@gmail.com', member_nickname='미정', member_intro='안녕하세요, 미정에요.',
    #            member_intro_detail='예술과 디자인에 관심이 많아요.'),
    #     Member(member_email='test13@gmail.com', member_nickname='준서', member_intro='안녕하세요, 준서입니다.',
    #            member_intro_detail='독서와 영화 감상을 좋아합니다.'),
    #     Member(member_email='test14@gmail.com', member_nickname='하윤', member_intro='안녕하세요, 하윤이에요.',
    #            member_intro_detail='다양한 문화를 배우고 싶어요.'),
    #     Member(member_email='test15@gmail.com', member_nickname='시우', member_intro='안녕하세요, 시우입니다.',
    #            member_intro_detail='음악과 여행을 사랑합니다.'),
    #     Member(member_email='test16@gmail.com', member_nickname='민서', member_intro='안녕하세요, 민서에요!',
    #            member_intro_detail='새로운 사람들과 어울리는 걸 좋아해요.'),
    #     Member(member_email='test17@gmail.com', member_nickname='건우', member_intro='안녕하세요, 건우입니다.',
    #            member_intro_detail='스포츠와 활동을 즐겨요.'),
    #     Member(member_email='test18@gmail.com', member_nickname='예나', member_intro='안녕하세요, 예나에요.',
    #            member_intro_detail='다양한 문화를 배우고 경험하고 싶어요.'),
    #     Member(member_email='test19@gmail.com', member_nickname='서준', member_intro='안녕하세요, 서준입니다.',
    #            member_intro_detail='음악과 예술을 즐기는 걸 좋아합니다.'),
    #     Member(member_email='test20@gmail.com', member_nickname='소희', member_intro='안녕하세요, 저는 소희에요.',
    #            member_intro_detail='새로운 친구를 사귀고 싶어요.'),
    #     Member(member_email='test21@gmail.com', member_nickname='태영', member_intro='안녕하세요, 태영입니다.',
    #            member_intro_detail='여행과 모험을 좋아합니다.'),
    #     Member(member_email='test22@gmail.com', member_nickname='예린', member_intro='안녕하세요, 예린이에요.',
    #            member_intro_detail='예술과 디자인에 관심이 많아요.'),
    #     Member(member_email='test23@gmail.com', member_nickname='건호', member_intro='안녕하세요, 건호입니다.',
    #            member_intro_detail='독서와 영화 감상을 좋아해요.'),
    #     Member(member_email='test24@gmail.com', member_nickname='민지', member_intro='안녕하세요, 민지에요.',
    #            member_intro_detail='새로운 경험을 찾고 있어요.'),
    #     Member(member_email='test25@gmail.com', member_nickname='유준', member_intro='안녕하세요, 유준입니다.',
    #            member_intro_detail='스포츠와 활동을 즐겨요.'),
    #     Member(member_email='test26@gmail.com', member_nickname='예림', member_intro='안녕하세요, 예림이에요.',
    #            member_intro_detail='다양한 문화를 배우고 싶어요.'),
    #     Member(member_email='test27@gmail.com', member_nickname='민재', member_intro='안녕하세요, 민재입니다.',
    #            member_intro_detail='음악과 예술을 즐기는 걸 좋아합니다.'),
    #     Member(member_email='test28@gmail.com', member_nickname='하은', member_intro='안녕하세요, 하은이에요!',
    #            member_intro_detail='새로운 친구를 사귀고 싶어요.'),
    #     Member(member_email='test29@gmail.com', member_nickname='주원', member_intro='안녕하세요, 주원입니다.',
    #            member_intro_detail='여행과 모험을 좋아합니다.'),
    #     Member(member_email='test30@gmail.com', member_nickname='지민', member_intro='안녕하세요, 지민이라고 해요.',
    #            member_intro_detail='예술과 문화를 즐기는 걸 좋아해요.')
    # ])


class Lesson(TestCase):

    Lesson.objects.bulk_create([
        Lesson(post_title='영어', post_content='영어과외', post_view_count=12, post_status='Y', member_id=18),
    ])


class LessonLike(TestCase):
    pass
    # LessonLike.objects.bulk_create([
    #     LessonLike(member_id=16, lesson_id=50),
    #     LessonLike(member_id=18, lesson_id=50),
    #     LessonLike(member_id=17, lesson_id=50),
    #     LessonLike(member_id=2, lesson_id=50),
    #     LessonLike(member_id=1, lesson_id=50),
    #  ])


class Helpers(TestCase):
    pass
      # Helpers.objects.bulk_create([
      #   Helpers(post_title='도움 제목9', post_content='도움내용1', post_status='Y', member_id=18),
      # ])


class HelpersLike(TestCase):
    pass
    # HelpersLike.objects.bulk_create([
    #     HelpersLike(member_id=16, helpers_id=50),
    #
    # ])


class Event(TestCase):
    pass
    # status = "N"
    # keyword = "이벤트"
    # events = Event.objects.filter(post_status=status).filter(
    #     Q(post_title__contains=keyword) | Q(post_content__contains=keyword)).order_by('-id').values('post_status')
    # print(events)

    # Event.objects.bulk_create([
    #     Event(post_title='이벤트11', post_content='이벤트에요10', post_status='Y', member_id=18, event_location='강남', event_latitude=0.10, event_longitude=2.2),
    #
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

# class MemberFile(TestCase):
    # MemberFile.objects.bulk_create([
    #     MemberFile(image='', file_type='P', member_id='21'),
    #     MemberFile(image='', file_type='P', member_id='22'),
    #     MemberFile(image='', file_type='P', member_id='23'),
    #     MemberFile(image='', file_type='P', member_id='24'),
    #     MemberFile(image='', file_type='P', member_id='25'),
    #     MemberFile(image='', file_type='P', member_id='26'),
    #     MemberFile(image='', file_type='P', member_id='27'),
    #     MemberFile(image='', file_type='P', member_id='28'),
    #     MemberFile(image='', file_type='P', member_id='29'),
    #     MemberFile(image='', file_type='P', member_id='30'),
    #     MemberFile(image='', file_type='P', member_id='31'),
    #     MemberFile(image='', file_type='P', member_id='32'),
    #     MemberFile(image='', file_type='P', member_id='33'),
    #     MemberFile(image='', file_type='P', member_id='34'),
    #     MemberFile(image='', file_type='P', member_id='35'),
    #     MemberFile(image='', file_type='P', member_id='36'),
    #     MemberFile(image='', file_type='P', member_id='37'),
    #     MemberFile(image='', file_type='P', member_id='38'),
    #     MemberFile(image='', file_type='P', member_id='39'),
    #     MemberFile(image='', file_type='P', member_id='40'),
    #     MemberFile(image='', file_type='P', member_id='41'),
    #     MemberFile(image='', file_type='P', member_id='42'),
    #     MemberFile(image='', file_type='P', member_id='43'),
    #     MemberFile(image='', file_type='P', member_id='44'),
    #     MemberFile(image='', file_type='P', member_id='45'),
    #     MemberFile(image='', file_type='P', member_id='46'),
    #     MemberFile(image='', file_type='P', member_id='47'),
    #     MemberFile(image='', file_type='P', member_id='48'),
    #     MemberFile(image='', file_type='P', member_id='49'),
    #     MemberFile(image='', file_type='P', member_id='50')

    # ])