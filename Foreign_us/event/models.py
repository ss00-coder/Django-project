from django.db import models

from Foreign_us.models import Post, Reply
from member.models import Member


# Create your models here.
class Event(Post):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_event'


class EventFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='event/%Y/%m/%d')
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_event_file"


class EventLike(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_event_like"


class EventReply(Reply):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_event_reply"