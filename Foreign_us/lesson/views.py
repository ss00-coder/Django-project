from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.models import LessonFile, Lesson, LanguageTag
from member.models import Member, MemberFile


# Create your views here.
class LessonListView(View):
    def get(self, request):
        return render(request, 'lesson/list.html')


class LessonListAPI(APIView):
    def get(self, request, page, type):
        size = 7
        offset = (page - 1) * size
        limit = page * size
        all_posts = list(Lesson.objects.order_by('-id').all())

        if type == 'popular_post':
            all_posts = list(Lesson.objects.order_by('-post_view_count').all())


        posts = []
        for i in range(len(all_posts)):
            id = all_posts[i].id
            member_files = Member.objects.get(id=Lesson.objects.get(id=id).member_id).memberfile_set.filter(file_type="P").values('image')
            lesson_file = LessonFile.objects.filter(lesson_id=id)
            post = Lesson.objects.filter(id=id).annotate(post_file=lesson_file.values('image')[:1], member_file=member_files).values('id', 'created_date', 'post_title', 'post_content', 'post_view_count', 'post_file', 'member__member_nickname', 'member_file')
            posts.append(post)

        posts = posts[offset:limit + 1]
        # posts = list(Notice.objects.order_by('-id').all())[offset:limit + 1]
        hasNext = False

        if len(posts) > size:
            hasNext = True
            posts.pop(size)


        context = {
            # 'posts': NoticeSerializer(posts, many=True).data,
            'posts': posts,
            'hasNext': hasNext
        }

        # return Response(posts)
        return Response(context)


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
