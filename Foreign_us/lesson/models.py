from django.db import models

from Foreign_us.models import Post, Reply
from member.models import Member


# Create your models here.
class Lesson(Post):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_lesson'


class LessonFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='lesson/%Y/%m/%d')
    lesson = models.ForeignKey(Lesson, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_lesson_file"


class LessonLike(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_lesson_like"


class LessonReply(Reply):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_lesson_reply"


class LanguageTag(models.Model):
    lesson = models.ForeignKey(Lesson, null=False, on_delete=models.CASCADE)
    language_type = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = "tbl_language_tag"