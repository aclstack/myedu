from django.db import models

# Create your models here.

class Message(models.Model):
    # verbose_name 表注释, primary_key设置主键
    name = models.CharField(max_length=20, verbose_name="姓名", primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=128, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        verbose_name = "留言信息"
        # 如果不设置verbose_name_plural，后台系统会显示为 verbose_name + s
        verbose_name_plural = "verbose_name"
        # 指定表名称，默认为Class名
        db_table = "message"