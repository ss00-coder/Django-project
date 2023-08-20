from django.db import models


# Create your models here.
class Period(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(Period):
    POST_STATUS = [
        ('Y', '게시 완료'),
        ('N', '임시 저장')
    ]

    post_title = models.CharField(max_length=200, null=False, blank=True)
    post_content = models.CharField(max_length=500, null=False, blank=True)
    post_view_count = models.PositiveIntegerField(default=0, null=False)
    post_status = models.CharField(max_length=1, blank=False, null=False, choices=POST_STATUS, default='Y')

    class Meta:
        abstract = True


class Message(Period):
    MESSAGE_STATUS = [
        ('Y', '읽음'),
        ('N', '읽지 않음')
    ]

    message_title = models.CharField(max_length=200, null=False, blank=True)
    message_content = models.CharField(max_length=500, null=False, blank=True)
    message_status = models.CharField(max_length=1, blank=False, null=False, choices=MESSAGE_STATUS, default='N')

    class Meta:
        abstract = True

# class File(Period):
#     image = models.ImageField(null=False, blank=False, upload_to='file/%Y/%m/%d')
#
#     class Meta:
#         abstract = True

class Reply(Period):
    reply_content = models.CharField(max_length=500, null=False, blank=True)

    class Meta:
        abstract = True