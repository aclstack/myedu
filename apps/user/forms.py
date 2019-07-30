# -*- coding:utf-8 -*-
# author: lyl
from django import forms
from captcha.fields import CaptchaField
import redis
from myedu.settings import REDIS_HOST, REDIS_PORT

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    # 验证指定字段,clean_字段名
    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        # decode_responses 解码否则会呈现 b'xxxx'的形式
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, charset="utf8", decode_responses=True)
        r_code = r.get(str(mobile))
        if r_code != code:
            # 验证失败抛出异常
            raise forms.ValidationError('验证码错误!!!!!')
        return self.cleaned_data

