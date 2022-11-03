from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlretrieve
from urllib import parse
import json
import re
import time
import socket
import os

socket.setdefaulttimeout(2)

someone = "刘涛"
someone_url_encode = parse.quote(someone)

root_url_bing = "https://cn.bing.com"
root_img_url_bing = "https://cn.bing.com/images/search?qs=HS&form=QBILPG&sp=1&sc=1-0&cvid=3D1922293241455E98107B88C986C5D6&first=1&tsc=ImageHoverTitle&q=" + someone_url_encode

root_url_baidu = "https://image.baidu.com"
root_img_url_baiduj = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" + someone_url_encode

# print(root_img_url_bing)
img_dest_dir = "E:\\studying\\img_lt\\"
data_count = 0
need_count = 1000

head = {
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE'}


def fetch_bing_pic(img_hover_url):
    global data_count
    print(data_count)
    print(img_hover_url)
    req = request.Request(img_hover_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    pic_fall = soup.find(id='mmComponent_images_1')
    next_url = root_url_bing + pic_fall.attrs['data-nexturl']
    # print(next_url)
    print()

    for tag in soup.find_all(class_='iusc'):
        # print(tag)
        img_detail = tag.attrs['m']
        img_detail_json = json.loads(img_detail)
        # print(img_detail_json)
        img_detail_url = img_detail_json['murl']
        img_file_name = img_detail_json['cid']
        img_dest_path = os.path.join(img_dest_dir,img_file_name + ".jpg")
        try:
            if os.path.exists(img_dest_path):
                data_count = data_count + 1
                continue
            time.sleep(0.3)
            urlretrieve(img_detail_url, img_dest_path)
            data_count = data_count + 1
            # print()
        except Exception:
            print(img_detail_url)
            continue
        if data_count > need_count:
            exit(0)
    fetch_bing_pic(next_url)


head = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': 'text/html,application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE'}

request_baidu_json_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8783002160215605263&ipn=rj&ct=201326592&is=&fp=result&fr=&word=" + someone_url_encode + "&cg=star&queryWord=" + someone_url_encode + "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&gsm=1e&"


def fetch_baidu_pic(img_hover_url):
    global data_count
    print(data_count)
    print(img_hover_url)
    req = request.Request(img_hover_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('ISO-8859-1')
    img_total_json = json.loads(html)
    for data in img_total_json['data']:
        file_suffix = "jpg"
        img_file_name = data_count
        if 'shituToken' in data and len(data['shituToken']) > 0:
            img_file_name = "baidu_" + data['shituToken']
        if 'type' in data and len(data['type']) > 0:
            file_suffix = data['type']
        if 'replaceUrl' in data:
            img_detail_url = data['replaceUrl'][0]['ObjURL']
            img_dest_path = os.path.join(img_dest_dir, img_file_name + "." + file_suffix)
            try:
                if os.path.exists(img_dest_path):
                    data_count = data_count + 1
                    continue
                time.sleep(0.3)
                urlretrieve(img_detail_url, img_dest_path)
                data_count = data_count + 1
                # print()
            except Exception:
                print(img_detail_url)
                continue
            if data_count > need_count:
                exit(0)
                break
    next_url = get_json_url(data_count, 60)
    fetch_baidu_pic(next_url)


def get_json_url(current_num, page_num):
    page = int(current_num / page_num)
    total_num = (page + 1) * page_num
    rn = str(page_num)
    pn = str(total_num)
    result = "rn=" + rn + "&pn=" + pn
    return request_baidu_json_url + result

if not os.path.exists(img_dest_dir):
    os.mkdir(img_dest_dir)
fetch_bing_pic(root_img_url_bing)
# fetch_baidu_pic(get_json_url(0, 60))
# print(get_json_url(0, 60))