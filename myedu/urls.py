"""myedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from myedu.settings import MEDIA_ROOT

import xadmin
from apps.user.views import LoginView, LogoutView, SendSmsView, DynamicLoginView, RegisterView
from apps.organizations.views import OrgView

# CBV(class base view)
# FBV(function base view)
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 使用django模块直接返回html
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    # name用于前端接收URL地址,如果前端引用不存在的值则会报错
    path('login/', LoginView.as_view(), name='login'),
    path('d_login/', DynamicLoginView.as_view(), name='d_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    # 短信验证相关页面
    # -------------------
    url(r'^captcha/', include('captcha.urls')),
    # 去除对send_sms的csrf验证
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),
    # -------------------

    # 机构相关页面
    # url('^org_list/', OrgView.as_view(), name='org_list'),
    # organizations为app_name 可以在这指定也可在include的urls.py指定
    url('^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),

    # 上传文件访问url
    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]

### 编写一个view的几个步骤
'''
1、view 代码
2、配置URL
3、修改HTML页面中相关的地址
'''