from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # 장고 모델인 Post는 DB에 저장됨
    title = models.CharField(max_length=200) # 글자수가 제한된 텍스트 정의
    text = models.TextField() # 글자수 제한 없는 긴 텍스트
    created_date = models.DateTimeField( # 날짜와 시간
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank = True, null = True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

