from django.db import models

from Foreign_us.models import Message
from member.models import Member


# Create your models here.
class ReceiveMessage(Message):
    send_member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE, related_name='send_member')
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_receive_message"


class SendMessage(Message):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    message = models.ForeignKey(ReceiveMessage, null=True, on_delete=models.CASCADE)
    receive_member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE, related_name='receive_member')

    class Meta:
        db_table = "tbl_send_message"


class ReceiveMessageFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='receive_message/%Y/%m/%d')
    receive_message = models.ForeignKey(ReceiveMessage, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_receive_message_file"


class SendMessageFile(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='send_message/%Y/%m/%d')
    send_message = models.ForeignKey(SendMessage, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_send_message_file"