from django.db import models

# Create your models here.
from common.models import CommonModel

# Subscriber : Subscribed_to = N : M

class Subscription(CommonModel):
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers') # 역참조
