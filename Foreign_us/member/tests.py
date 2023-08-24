from django.test import TestCase

from member.models import MemberFile


# Create your tests here.
class MemberFileTest(TestCase):
    # image = models.ImageField(null=False, blank=False, upload_to='member/%Y/%m/%d')
    # member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    # file_type = models.CharField(max_length=1, blank=False, null=False, choices=MEMBER_FILE_TYPE, default='P')

    MemberFile.objects.create(MemberFile(image='member/2023/08/23/dogs.jpg'))
    MemberFile.objects.create(MemberFile(image='member/2023/08/23/background.png'))