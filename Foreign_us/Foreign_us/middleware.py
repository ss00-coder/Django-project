from message.models import ReceiveMessage

# custom middleware - class
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화

    def __call__(self, request):
        member_email = request.session.get('member_email')

        if member_email:
            unread_message_count = ReceiveMessage.objects.filter(member__member_email=member_email,
                                                                 message_status='N').count()
            request.session['unread_message_count'] = unread_message_count

        response = self.get_response(request)

        # 뷰가 호출된 뒤에 실행될 코드들


        return response