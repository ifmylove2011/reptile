from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlretrieve
from urllib import parse
import re
import time

someone = "刘亦菲"
someone_url_encode = parse.quote(someone)
test_url = "https://cn.bing.com/images/search?q=%E5%88%98%E4%BA%A6%E8%8F%B2&form=HDRSC2&first=1&tsc=ImageHoverTitle&cw=1177&ch=891"
root_url_bing = "https://cn.bing.com"
root_img_url_bing = "https://cn.bing.com/images/search?qs=HS&form=QBILPG&sp=1&sc=1-0&cvid=3D1922293241455E98107B88C986C5D6&first=1&tsc=ImageHoverTitle&q=" + someone_url_encode

head = {
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE'}


print(root_img_url_bing)

def fetch_main_fall(img_url):
    req = request.Request(img_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    pic_fall = soup.find(id='b_content').find(id='mmComponent_images_1')
    next_url = root_url_bing+pic_fall.attrs['data-nexturl']
    print(next_url)

    for tag in soup.find_all(class_='iusc'):
        img_detail_url = root_url_bing+tag.attrs['href']
        print(img_detail_url)
        urlretrieve("https://n.sinaimg.cn/sinakd10111/696/w640h856/20200808/8acf-ixkvvue1874391.jpg","1.jpg")

        break

def download(url,filename):
    req = request.Request(url, headers=head)
    responese = request.urlopen(req)
    with open(filename, "wb") as code:
        code.write(responese.content)




fetch_main_fall(root_img_url_bing)
