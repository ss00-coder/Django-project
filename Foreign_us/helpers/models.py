from django.db import models

from Foreign_us.models import Post, Reply
from member.models import Member


# Create your models here.
class Helpers(Post):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_helpers'


class HelpersFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='helpers/%Y/%m/%d')
    helpers = models.ForeignKey(Helpers, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_helpers_file"


class HelpersLike(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    helpers = models.ForeignKey(Helpers, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_helpers_like"


class HelpersReply(Reply):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    helpers = models.ForeignKey(Helpers, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_helpers_reply"