from urllib import request
from urllib import error

url = "http://www.douyu.com/Jack_Cui.html"
req = request.Request(url)
try:
    responese = request.urlopen(req)
    # html = responese.read()
except error.HTTPError as e:
    print(e.code)
    print(e.reason)