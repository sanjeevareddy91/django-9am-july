from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team_Info(models.Model):
    team_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=4)
    team_logo = models.ImageField(null=True,blank=True)
    captain_name = models.CharField(max_length=25)
    started_year = models.IntegerField(max_length=4)

    class Meta:
        db_table = 'team_info'

    def __str__(self):
        return self.team_name

class RegisteredUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    otp = models.CharField(max_length=6,null=True,blank=True)

    class Meta:
        db_table = 'registereduser'
