from django.db import models

# Create your models here.
from common.models import CommonModel

class Comment(CommonModel):
    # user : Comment = 1 : N
    # video : comment = 1 : N
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    # 정보 통신 보호법 + Euro 6

    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # 대댓글
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)