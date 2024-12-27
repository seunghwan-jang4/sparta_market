from django.db import models
from django.conf import settings
import re   # 정규표현식 라이브러리
from django.core.exceptions import ValidationError  # 유효성 검사 예외 처리

# 상품 이미지를 저장할 경로를 생성하는 함수
def product_image_path(instance, filename):
    return f'product_images/{instance.user.username}/{filename}'

# 파이썬의 정규표현식
#해시태그가 유효한지 검사하는 사용자 정의 함수를 선언. (해시태그는 띄어쓰기 특수문자를 허용하지 않는다.)
def validation_hashtag(value):
    if not re.match(r'^[0-9a-zA-Z_]+$', value): # 정규표현식 => 공백 / 특수문자를 불허하는 코드.
        raise ValidationError('해시태그는 알파벳, 숫자, 언더스코어만 가능합니다!')

# 해시태그를 저장하는 모델.
class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validation_hashtag])
    
    def __str__(self):
        return f'#{self.name}'

# 사용자의 등록한 상품을 저장하는 모델
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products') #상품을 등록한 사용자.
    title = models.CharField(max_length=100)    # 상품 제목.
    description = models.TextField() # 상품 설명.
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True) # 상품 이미지.
    created_at = models.DateTimeField(auto_now_add=True) # 상품 등록일.
    
    #user like(좋아요)는 ManytoManyField 다대다 관계를 설정 가능.(user 모델과)
    # 상품에 좋아요가 없을 수도 있기 때문에, blank=True 
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products', blank=True) # 상품에 좋아요한 사용자들.
    # 상품과 연결 돼 있는 해시태그 = 다대다 관계
    hashtags = models.ManyToManyField(HashTag, related_name='products', blank=True)
    views = models.PositiveIntegerField(default=0)  # 상품 조회수.
    
    # 상품에 좋아요를 누른 사용자 수
    def like_count(self):
        return self.likes.count()
    
    # 상품의 제목을 문자열로 반환
    def __str__(self):
        return self.title