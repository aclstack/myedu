# -*- coding:utf-8 -*-
# author: lyl
import requests
import xmltodict


def send_single_sms(info,code, mobile):
    print(mobile, code)
    msg = {
        'mobile': mobile,
        'code': 0,
        # 错误信息
        'msg' : ''

    }
    return msg
# 信息保密，采用伪代码实现
    header = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"}
    url = 'http://cf.51welink.com/submitdata/Service.asmx/g_Submit'

    args = {
        'sname': '',
        'spwd': '',
        'sprdid': '',
        'scorpid': '',
        'sdst': mobile,
        'smsg': str(code) + ''

    }

    res = requests.get(url=url, params=args, headers=header)

    return res


# res = send_single_sms('测试消息', )
# res_str = xmltodict.parse(res.text)
# import json
#
# jsonstr = json.dumps(res_str,indent=1)
# res_json = json.loads(jsonstr)
# print(res_json)
# print("##############")
# print(res_json['CSubmitState']['State'])
# print(res_json['CSubmitState']['MsgState'])


