import urllib3
from urllib import parse
from lxml import etree
import json

#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()


# 通过request()方法创建一个请求：
# r = http.request('GET', 'http://www.baidu.com/')
r = http.request('GET', 'https://www.baidu.com/s?word=selenium&tn=50000022_hao_pg&ie=utf-8&sc=UWd1pgw-pA7EnHc1FMfqnHRYPHD3n1c3rjn3PauW5y99U1Dznzu9m1YYPHb1PWbzPHT&ssl_sample=s_11&srcqid=2675966891224638233&f=3&rsp=0&H123Tmp=nu')
print(r.status) # 200

# print(r.data.decode())

# 获得html源码,utf-8解码
# print(r.data.decode())



# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
# }
# r = http.request('GET',
#                  'https://www.baidu.com/s?',
#                  fields={'wd': 'hello'},
#                  headers=header)
# print(r.status)  # 200
# print(r.data.decode())