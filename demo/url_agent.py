# -*- coding: UTF-8 -*-
from urllib import request

# 用户代理

# 以CSDN为例，CSDN不更改User Agent是无法访问的
# url = 'http://www.csdn.net/'
# head = {}
# # 写入User Agent信息
# head[
#     'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
# # 创建Request对象
# req = request.Request(url, headers=head)
# # 传入创建好的Request对象
# response = request.urlopen(req)
# # 读取响应信息并解码
# html = response.read().decode('utf-8')
# # 打印信息
# print(html)

# # 以CSDN为例，CSDN不更改User Agent是无法访问的
# url = 'http://www.csdn.net/'
# # 创建Request对象
# req = request.Request(url)
# # 传入headers
# req.add_header('User-Agent',
#                'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
# # 传入创建好的Request对象
# response = request.urlopen(req)
# # 读取响应信息并解码
# html = response.read().decode('utf-8')
# # 打印信息
# print(html)



# 地址代理
# 访问网址
url = 'http://www.whatismyip.com.tw/'
# 这是代理IP
proxy = {'http': '183.159.81.229:18118'}
# 创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
# 创建Opener
opener = request.build_opener(proxy_support)
# 添加User Angent
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
# 安装OPener
request.install_opener(opener)
# 使用自己安装好的Opener
response = request.urlopen(url)
# 读取相应信息并解码
html = response.read().decode("utf-8")
# 打印信息
print(html)
