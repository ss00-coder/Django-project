from django.shortcuts import render, redirect
from django.views import View

from lesson.models import LessonFile, Lesson
from member.models import Member


# Create your views here.
class LessonListView(View):
    def get(self, request):
        return render(request, 'lesson/list.html')


class LessonDetailView(View):
    def get(self, request):
        return render(request, 'lesson/detail.html')


class LessonWriteView(View):
    def get(self, request, post_id=None):
        member = Member.objects.get(member_email=request.session['member_email'])
        member_profile_img = "member/profile_icon.png"
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image
        if Lesson.objects.filter(id=post_id):
            post = Lesson.objects.get(id=post_id)
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'member': member,
                'post_id': post_id,
            }
        else:
            context = {
                'member_file': member_profile_img,
                'post_title': "",
                'post_content': "",
                'post_status': "",
                'member': "",
                'post_id': 0,
            }


        return render(request, 'lesson/write.html', context)

    def post(self, request, post_id):
        member = Member.objects.get(member_email=request.session['member_email'])
        datas = request.POST
        files = request.FILES

        lesson_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'member': member,
        }

        if Lesson.objects.filter(id=post_id):
            Lesson.objects.filter(id=post_id).update(**lesson_datas)
            lesson_post = Lesson.objects.get(id=post_id)

            if files:
                LessonFile.objects.filter(lesson_id=post_id).delete()
                for file in files.getlist('post_file'):
                    LessonFile.objects.create(image=file, lesson=lesson_post)

        else:
            lesson_post = Lesson.objects.create(**lesson_datas)
            if files:
                for file in files.getlist('post_file'):
                    LessonFile.objects.create(image=file, lesson=lesson_post)


        return redirect('lesson:list-init')


class LessonReviewDetailView(View):
    def get(self, request):
        return render(request, 'lesson/review-detail.html')


class LessonReviewWriteView(View):
    def get(self, request):
        return render(request, 'lesson/review-write.html')
