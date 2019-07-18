# -*- coding:utf-8 -*-
# author: lyl
import xadmin


from apps.courses.models import Course, Lesson, Video, CourseResource

# 定义title以及页脚信息
class GlobalSettings(object):
  site_title = '力哥教育后台管理系统'
  site_footer = '力哥教育'
  # 折叠菜单，并显示子类数量，如果菜单比较多建议使用
  # menu_style = "accordion"

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'teacher']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    ## __取外键信息teacher__name则表示为取teacher name
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'add_time', 'students']
    list_editable = ['degree', 'desc']

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
# title and footer
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)

# themes
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)