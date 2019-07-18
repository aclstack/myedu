from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class BaseModel(models.Model):
    # 如果datetime.now()则时间会固定
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 定义不生成此表，仅做继承使用
        abstract = True


class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    # 设置图片上传路径
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg", verbose_name='用户头像')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            self.username = self.nick_name
        return self.username


