from django.db.models import F
from django.shortcuts import render
from django.views import View

from lesson.models import Lesson
from member.models import Member


# Create your views here.
class MyProfileView(View):
    # 프로필 사이드바 닉네임
    def get(self, request):
        # email = request.session['member_email'] #(멤버이메일값)
        # print(Member.objects.annotate(email=F('member_email')).values('member_nickname'))
        # member = Member.objects.get(member_email=email)
        member = Member.objects.filter(member_nickname='짱구')
        # print(member[0].member_nickname)  // 이건 필터
        nicknames = {'nickname':member[0].member_nickname}
        # print(nicknames)
        # print(nicknames)
        return render(request, 'mypage/myprofile.html', nicknames)


    # def post(self, request, *args, **kwargs):
    #     token, member_email, member_nickname, member_birth = request.POST.values()
    #     Member.objects.create(member_email=member_email, member_password=member_password, member_name=member_name,
    #                           member_age=member_age, member_birth=member_birth)
    #     # 이동할 urls 경로를 작성한다.
    #     return redirect('/member/login')


class MyLessonView(View):
    def get(self, request):
        five_lessons =Lesson.objects.all()[0:5]
        print(five_lessons)

        context = {
            "lessons" : five_lessons
        }

        return render(request, 'mypage/mylesson.html', context)



class MyLessonReviewView(View):
    def get(self, request):
        return render(request, 'mypage/mylesson-review.html')


class MyHelpersView(View):
    def get(self, request):
        return render(request, 'mypage/myhelpers.html')


class MyEventView(View):
    def get(self, request):
        return render(request, 'mypage/myevent.html')


class MyMessageListView(View):
    def get(self, request):
        return render(request, 'message/list.html')


class MyMessageDetailView(View):
    def get(self, request):
        return render(request, 'message/detail.html')


class MyMessageWriteView(View):
    def get(self, request):
        return render(request, 'message/write.html')


class MyPayView(View):
    def get(self, request):
        return render(request, 'mypage/mypay.html')
