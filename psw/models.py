from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    sex = models.CharField(max_length=2)
    birthday = models.DateTimeField()

    def __str__(self):
        return self.name


class Chain(models.Model):
    user_no = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    obj = models.CharField(max_length=50)
    user = models.CharField(max_length=20)
    psw = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    remarks = models.CharField(max_length=500)
    reg_date = models.DateTimeField()

    def __str__(self):
        return self.obj
