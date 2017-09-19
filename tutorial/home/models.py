from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True) #
    updated = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner',null=True) #ManyToManyField같은 관계를 형성하면 자동으로 related_name을 부여한다.

    @classmethod
    def make_friend(cls, current_user, new_frined):  #current_user는 현재 로그인한 user, new_frined와 관계를 만든다.
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_frined)


    @classmethod
    def lose_friend(cls, current_user, new_frined):  #current_user는 현재 로그인한 user, new_frined와 관계를 만든다.
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_frined)
