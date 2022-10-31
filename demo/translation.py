from urllib import parse
from urllib import request
import json

Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
# i:tomorrow
# from:AUTO
# to:AUTO
# smartresult:dict
# client:fanyideskweb
# salt:1524102618041
# sign:28667d7750f60a8f8d630fb856bb19be
# doctype:json
# version:2.1
# keyfrom:fanyi.web
# action:FY_BY_REALTIME
# typoResult:false
# 创建Form_Data字典，存储上图的Form Data
Form_Data = {}
Form_Data['type'] = 'AUTO'
Form_Data['to'] = 'AUTO'
Form_Data['smartresult'] = 'fanyideskweb'
Form_Data['salt'] = 1524102618041
Form_Data['sign'] = '28667d7750f60a8f8d630fb856bb19be'
Form_Data['doctype'] = 'json'
Form_Data['version'] = 2.1
Form_Data['keyfrom'] = 'fanyi.web'
Form_Data['action'] = 'FY_BY_REALTIME'
Form_Data['i'] = 'tomorrow'
Form_Data['typoResult'] = 'false'
# 使用urlencode方法转换标准格式
data = parse.urlencode(Form_Data).encode('utf-8')
# 传递Request对象和转换完格式的数据
response = request.urlopen(Request_URL, data)
# 读取信息并解码
html = response.read().decode('utf-8')
# 使用JSON
translate_results = json.loads(html)
# 找到翻译结果
translate_results = translate_results['translateResult'][0][0]['tgt']
# 打印翻译信息
# {
# 	"translateResult": [
# 		[{
# 			"tgt": "明天",
# 			"src": "tomorrow"
# 		}]
# 	],
# 	"errorCode": 0,
# 	"type": "en2zh-CHS",
# 	"smartResult": {
# 		"entries": ["", "n. 明天；未来\r\n", "adv. 明天；未来地（等于to-morrow）\r\n"],
# 		"type": 1
# 	}
# }
print("翻译的结果是：%s" % translate_results)
