from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def user_profile_image_path(instance, filename):
    return f'profile_images/{instance.username}/{filename}'

# 프로필 이미지, 팔로우 수, 팔로잉 수
class User(AbstractUser):
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank = True, null = True) # 프로필 이미지 경로를 지정. null = True 로써, 값이 없어도 허용.

    # 팔로우
    follows = models.ManyToManyField('self', symmetrical = False, related_name = 'followers', blank = True)
    # 팔로워 카운트
    @property
    def follower_count(self):
        return self.followers.count()
    # 팔로잉 카운트
    @property
    def following_count(self):
        return self.follows.count()
    # 객체를 문자열로 표현할 때 사용자 이름을 반환
    def __str__(self):
        return self.username