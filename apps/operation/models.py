from django.db import models
# 此方法返回 AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from apps.user.models import BaseModel
from apps.courses.models import Course

# 此项目已经定义UserProfile覆盖django默认user,如果后续使用默认user表，则改动太大，因此采用Django函数获取当前User表信息
UserProfile = get_user_model()

Favorite_Type = (
    (1, '课程'),
    (2, '课程机构'),
    (3, '讲师'),
)


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')

    class Meta():
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{cpirse}({mobile})".format(self.name, self.course_name, self.mobile)

class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    comments = models.CharField(max_length=200, verbose_name='评论内容')
    class Meta():
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments

class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    # 采用ID的方式避免后续增加收藏类型，更改表结构
    Favorite_id= models.IntegerField(verbose_name="数据id")
    Favorite_type = models.IntegerField(choices=Favorite_Type, default=1, verbose_name="收藏类型")
    class Meta():
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{user}_{id}".format(self.user.username, self.Favorite_id)

class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    message = models.CharField(max_length=200, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')

    class Meta():
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    class Meta():
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name