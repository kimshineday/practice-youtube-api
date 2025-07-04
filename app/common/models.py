from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 데이터 생성된 시간 
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 업데이트 된 시간 -> 업데이트 될 때마다 시간 변경

    class Meta:
        abstract = True # DB에 테이블 추가 X