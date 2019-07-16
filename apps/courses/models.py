from django.db import models

from apps.user.models import BaseModel
from apps.organizations.models import Teacher

"""
实体1 <关系> 实体2
课程 章节 课程资源 （一对多）
章节 视频   (一对多)
Course 课程基本信息
Lesson 章节信息
Video  视频
CourseResource  课程资源
"""

CLASS_LEVEL = (
    ('cj', '初级'),
    ('zj', '中级'),
    ('gj', '高级'),
)


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='讲师')
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    degree = models.CharField(verbose_name="难度", choices=CLASS_LEVEL, max_length=2)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(default=u'后端开发', max_length=20, verbose_name="课程类别")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    need_know = models.CharField(default="", verbose_name="课程须知", max_length=300)
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师告诉你")
    detail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面图", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

# 章信息
class Lesson(BaseModel):
    # on_delete 表示对应的外检数据被删除后，当前的数据应该怎么办,常用CASCADE、SET_NULL
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name

# 单节课程信息
class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    url = models.CharField(max_length=200, verbose_name=u'访问地址')

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

# 资料信息
class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name=u'名称')
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
