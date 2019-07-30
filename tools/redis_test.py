# -*- coding:utf-8 -*-
# author: lyl
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf8", decode_responses=True)

r.set('name', 'zhangsan')
r.expire('name', 1)
import time
time.sleep(1)
print(r.get('name'))
