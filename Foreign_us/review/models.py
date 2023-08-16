from django.db import models

from Foreign_us.models import Post, Reply
from member.models import Member


# Create your models here.
class Review(Post):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    reviewed_member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE, related_name='reviewed_member')

    class Meta:
        db_table = 'tbl_review'


class ReviewFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='review/%Y/%m/%d')
    review = models.ForeignKey(Review, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_review_file"


class ReviewLike(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_review_like"


class ReviewReply(Reply):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_review_reply"