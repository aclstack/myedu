from django.db import models
# 此方法返回 AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from apps.user.models import BaseModel
from apps.courses.models import Course

# 此项目已经定义UserProfile覆盖django默认user,如果后续使用默认user表，则改动太大，因此采用Django函数获取当前User表信息
UserProfile = get_user_model()

class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')

    class Meta():
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    comments = models.CharField(200, verbose_name='评论内容')
    class Meta():
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    teacher = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    class Meta():
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name