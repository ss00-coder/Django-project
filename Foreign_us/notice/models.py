from django.db import models

from Foreign_us.models import Post, Reply
from member.models import Member


# Create your models here.
class Notice(Post):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)


    def get_absolute_url(self, page):
        return f"/administrator/board/notice/detail/{self.id}/{page}"
    class Meta:
        db_table = 'tbl_notice'


class NoticeFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='notice/%Y/%m/%d')
    notice = models.ForeignKey(Notice, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_notice_file"


class NoticeLike(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_notice_like"


class NoticeReply(Reply):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_notice_reply"