import requests
from django.shortcuts import render, redirect, resolve_url
from django.views import View

from member.models import Member


# Create your views here.
class MemberLoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')


class KakaoView(View):
    def get(self, request):
        code = request.GET.get("code")
        print()
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=58c7a23bf4f0c4c562ce6e0fea062614&' \
                       'redirect_uri=http://localhost:10000/member/oauth/redirect&' \
                       f'code={code}'
        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
        info = response.json().get('kakao_account')
        nickname = info.get('profile').get('nickname')
        email = info.get('email')
        request.session['member_email'] = email
        request.session['access_token'] = access_token
        member = Member.objects.filter(member_email=email).first()
        request.session['member_type'] = member.member_type

        if not member:
            count = Member.objects.count() + 1
            Member.objects.create(member_email=email, member_nickname=f'유저{count}', member_intro="", member_intro_detail="")
            return redirect('mypage:myprofile')
        return redirect('/')


class MemberLogoutView(View):
    def get(self, request):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Authorization': f"Bearer {request.session['access_token']}",
        }
        response = requests.post(f"https://kapi.kakao.com/v1/user/logout", headers=headers)
        response.cookies.clear_session_cookies()
        request.session.flush()
        return redirect('/')


