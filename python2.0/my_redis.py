# -*- coding: UTF-8 -*-
from redis import Redis
啊=1
r = Redis(host='127.0.0.1')

r.zadd('z2', {'你a':0,'你好':0, '你好啊':0,'你不':0, '打我':0, '打不':0})
print r.zadd('z2',{'你1': 0})
for i in r.zrange('z2', 0, -1):
    print i
