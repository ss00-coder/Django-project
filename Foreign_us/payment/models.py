from django.db import models

from Foreign_us.models import Period
from member.models import Member


# Create your models here.
class Payment(Period):
    PAY_STATUS = [
        ('Y', '결제 완료'),
        ('N', '결제 취소')
    ]

    LESSON_TYPE = [
        ('Y', '대면'),
        ('N', '비대면')
    ]

    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Member, null=False, on_delete=models.CASCADE, related_name='teacher')
    pay_status = models.CharField(max_length=1, blank=False, null=False, choices=PAY_STATUS, default='Y')
    lesson_type = models.CharField(max_length=1, blank=False, null=False, choices=LESSON_TYPE, default='Y')


    class Meta:
        db_table = "tbl_payment"