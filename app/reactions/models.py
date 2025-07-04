from django.db import models

# Create your models here.
from common.models import CommonModel

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    # reaction = like(+1), dislike(-1), no-reaction(0) > choice 옵션
    # 데이터를 제한을 둬서 고르게 하는 방법.
    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'DisLike'),
        (NO_REACTION, 'No Reacion')
    ) # tuple 형태.

    reaction = models.IntegerField(
        choices = REACTION_CHOICES,
        default = NO_REACTION
    )

    # user : Reation = 1 : N (FK)
    # video : Reation = 1 : N (FK)

# import로 불러올 시 Circular Import Error 발생 가능성 있음.
# 'users.User' > users앱의 User 클래스 가져온다. django 시스템에서 사용할 수 있는 방법 (Lazy Relationship)