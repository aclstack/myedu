# -*- coding:utf-8 -*-
# author: lyl
from django import forms
from apps.operation.models import UserAsk

class AddAskForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=12,
                           error_messages={'required': '姓名填写错误',
                                           'min_length': '姓名长度至少为2位',
                                           'max_length': '姓名长度不能超过12位'
                                           })
    mobile = forms.CharField(required=True, min_length=11, max_length=11,
                             error_messages={'required': '手机号填写错误',
                                             'min_length': '手机号必须为11位',
                                             'max_length': '手机号必须为11位'
                                             })
    course_name = forms.CharField(required=True, min_length=2, max_length=20,
                                  error_messages={'required': '课程名填写错误',
                                                  'min_length': '课程长度至少为2位',
                                                  'max_length': '课程长度不能超过20位'
                                                  })



# 通过model生成form表单
class AddAskForm2(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']


    def clean_name(self):
        if  2< len(self.data.get('name'))< 12:
            pass
        else:
            raise forms.ValidationError('姓名长度为2到12位')

    def clean_mobile(self):
        if len(self.data.get('mobile')) != 11:
            raise forms.ValidationError('手机号填写错误')

    def clean_course_name(self):
        if  2< len(self.data.get('course_name'))< 12:
            pass
        else:
            raise forms.ValidationError('课程名填写错误')