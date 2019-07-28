# -*- coding:utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    # 下列字段需要和前端页面保持一致
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)
