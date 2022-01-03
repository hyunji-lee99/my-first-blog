from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # 모델을 정의하는 코드, 클래스명의 첫 글자는 항상 대문자로 작성.
    # models는 Post가 장고 모델임을 의미함. 이 코드때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게됨.
    # 속성을 정의하기 위해선 필드마다 어떤 종류의 데이터 타입을 가지는지 정해야 함. 데이터 타입에는 텍스트, 숫자, 날짜, 사용자 등이 있음.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자 수가 제한된 텍스트를 정의할 때 사용함. 글 제목과 같은 짧은 문자열 정보를 저장할 때 사용.
    text = models.TextField() #글자 수에 제한이 없는 긴 텍스트를 위한 속성.
    created_date = models.DateTimeField(
            default=timezone.now) #날짜와 시간
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #__str__을 호출하면 Post 모델의 제목 텍스트를 반환.

