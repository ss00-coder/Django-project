from django.shortcuts import render, redirect
from django.views import View

from lesson.models import LessonFile, Lesson, LanguageTag
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
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 멤버 프로필 이미지 없으면 기본 이미지로
        member_profile_img = "member/profile_icon.png"

        # 멤버의 프로필 이미지가 있으면 해당 이미지로
        if member.memberfile_set.filter(file_type='P'):
            member_profile_img = member.memberfile_set.get(file_type="P").image

        # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
        if Lesson.objects.filter(id=post_id):
            post = Lesson.objects.get(id=post_id)
            post_tags = LanguageTag.objects.filter(lesson_id=post_id)
            context = {
                'member_file': member_profile_img,
                'post_title': post.post_title,
                'post_content': post.post_content,
                'post_status': post.post_status,
                'member': member,
                'post_id': post_id,
                'post_tags': post_tags,
                'tag_delete': post_tags,
            }
        # 거짓이면 새로운 게시글 작성
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
        # 멤버 정보
        member = Member.objects.get(member_email=request.session['member_email'])

        # 작성 및 수정페이지에서 받아온 데이터 및 파일,태그
        datas = request.POST
        files = request.FILES

        # 받아온 태그가 있다면 해당 태그 값을 담고 없으면 None이다
        post_tags = dict(datas).get("post_tags")

        # lesson(게시글) 생성 및 업데이트 할때 넣을 데이터
        lesson_datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content'],
            'post_status': datas['post_status'],
            'member': member,
        }

        # 수정할 게시글 아이디가 맞다면 해당 게시글 수정
        if Lesson.objects.filter(id=post_id):
            Lesson.objects.filter(id=post_id).update(**lesson_datas)
            lesson_post = Lesson.objects.get(id=post_id)
            # 파일 업로드 시 전에 있던 파일 삭제 후 새로 받은 파일로 생성
            if files:
                LessonFile.objects.filter(lesson_id=post_id).delete()
                for file in files.getlist('post_file'):
                    LessonFile.objects.create(image=file, lesson=lesson_post)
            # 태그가 있다면 생성
            if post_tags:
                for tag in post_tags:
                    LanguageTag.objects.update_or_create(language_type=tag, lesson=lesson_post)
            # 하나라도 없으면 해당 게시글의 태그 전체삭제
            else:
                LanguageTag.objects.filter(lesson_id=post_id).delete()


        # 수정할 게시글이 없다면 새로운 게시글 생성
        else:
            lesson_post = Lesson.objects.create(**lesson_datas)
            # 파일 생성
            if files:
                for file in files.getlist('post_file'):
                    LessonFile.objects.create(image=file, lesson=lesson_post)

            # 태그 생성
            if post_tags:
                for tag in post_tags:
                    LanguageTag.objects.create(language_type=tag, lesson=lesson_post)


        return redirect('lesson:list-init')


class LessonReviewDetailView(View):
    def get(self, request):
        return render(request, 'lesson/review-detail.html')


class LessonReviewWriteView(View):
    def get(self, request):
        return render(request, 'lesson/review-write.html')
