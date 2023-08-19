from django.db import models

from Foreign_us.models import Period


# Create your models here.
class Member(Period):
    MEMBER_TYPE = [
        ('Y', '일반 회원'),
        ('N', '탈퇴 회원'),
        ('A', '관리자')
    ]

    member_email = models.CharField(max_length=200, unique=True, null=False, blank=False)
    member_nickname = models.CharField(max_length=200, unique=True, null=False, blank=False)
    member_intro = models.CharField(max_length=300, null=False, blank=False)
    member_intro_detail = models.TextField(blank=False, null=False)
    member_type = models.CharField(max_length=1, blank=False, null=False, choices=MEMBER_TYPE, default='Y')
    member_address = models.CharField(max_length=500, null=True)
    member_latitude = models.FloatField(null=True, blank=True)
    member_longitude = models.FloatField(null=True, blank=True)


    class Meta:
        db_table = "tbl_member"


class MemberSNS(models.Model):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    sns_type = models.CharField(max_length=200, null=False, blank=False)
    sns_url = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        db_table = "tbl_member_sns"


class MemberFile(models.Model):
    MEMBER_FILE_TYPE = [
        ('P', '프로필 사진'),
        ('B', '배경 사진')
    ]

    image = models.ImageField(null=False, blank=False, upload_to='member/%Y/%m/%d')
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=1, blank=False, null=False, choices=MEMBER_FILE_TYPE, default='P')

    class Meta:
        db_table = "tbl_member_file"