# 用于在中关村在线找到符合长度的显卡

from bs4 import BeautifulSoup
from urllib import request
import re
import time

GPU = "3080"
RE_MEASURE = r'(\d+[\.\d]+?)\S(\d+[\.\d]+?)\S(\d+[\.\d]+?)mm?'
MAX_LENGTH = 300

need_to_create_file = False

root_src_url = "https://detail.zol.com.cn"
root_vga_url = "https://detail.zol.com.cn/vga/"
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE'}


def fetch_info():
    gpu_list_url = fetch_vag_other_condition(fetch_vga_list_url(GPU))
    # gpu_urls = fetch_vga_detail_urls('https://detail.zol.com.cn/vga/s8467/')
    gpu_urls = fetch_vga_detail_urls(gpu_list_url)
    # print(gpu_urls)
    counter = 0
    for name, detail_url in gpu_urls.items():
        params_url = fetch_vga_params_url(detail_url)
        time.sleep(1)
        counter = counter + 1
        # print(counter)
        fetch_vga_params_info(name, params_url)
    # fetch_GPU_URLS('https://detail.zol.com.cn/vga/s8467/2.html')


def fetch_vga_list_url(GPU):
    vag_list_Url = ""
    req = request.Request(root_vga_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('GBK')
    soup = BeautifulSoup(html, 'lxml')

    # print(soup.prettify())

    for tag in soup.find(id='J_ParamItem2').find_all('a'):
        # print(tag.string.text)
        if re.match(r".*" + GPU + r"$", tag.string.text):
            print(tag)
            vag_list_Url = root_src_url + tag.attrs['href']
            print(vag_list_Url)
    return vag_list_Url


def fetch_vag_other_condition(vag_list_url):
    time.sleep(1)
    vga_other_list_url = ""
    req = request.Request(vag_list_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('GBK')
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find(id='J_otherItem').find_all('a'):
        if re.match(r"三风扇", tag.string.text):
            print(tag)
            vga_other_list_url = root_src_url + tag.attrs['href']
            print(vga_other_list_url)
    return vga_other_list_url


# 会有翻页，URL有所不同，因此会调用多次
def fetch_vga_detail_urls(vga_list_url):
    gpu_urls = {}
    req = request.Request(vga_list_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('GBK')
    soup = BeautifulSoup(html, 'lxml')

    for li in soup.find(id='J_PicMode').find_all('li'):
        if li is not None:
            a = li.find('a')
            if a is not None:
                gpu_urls[a.img.attrs['alt']] = root_src_url + a.attrs['href']

    next_page = soup.find(class_='small-page-next')
    if next_page is not None and next_page.has_attr('href'):
        next_list_url = root_src_url + next_page.attrs['href']
        print(next_list_url)
        time.sleep(1)
        gpu_urls.update(fetch_vga_detail_urls(next_list_url))

    print(len(gpu_urls))
    return gpu_urls


def fetch_vga_params_url(vag_detail_url):
    req = request.Request(vag_detail_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('GBK')
    soup = BeautifulSoup(html, 'lxml')

    params_page = soup.find(class_='_j_MP_more section-more')
    if params_page is not None:
        return root_src_url + params_page.attrs['href']


def fetch_vga_params_info(name, vag_params_url):
    # print(vag_params_url)
    req = request.Request(vag_params_url, headers=head)
    responese = request.urlopen(req)
    html = responese.read().decode('GBK')
    soup = BeautifulSoup(html, 'lxml')

    params_info = soup.find(class_='detailed-parameters')
    if params_info is not None:
        measure = params_info.find(text=re.compile(RE_MEASURE))
        if measure is not None:
            if need_to_create_file:
                write_to_file(vag_params_url + "\n" + name + " " + measure + "\r\n")
            if check_measure(measure.string):
                print()
                print(vag_params_url)
                print(name + "  " + measure)


def write_to_file(content):
    f = open("vga_info_" + GPU + ".txt", "a")
    f.write(content)
    f.close()


def check_measure(measure):
    result = re.match(RE_MEASURE, measure)
    if result is not None:
        a = result.group(1)
        b = result.group(2)
        c = result.group(3)
        return (200 < float(a) < MAX_LENGTH) or (200 < float(b) < MAX_LENGTH)
    return False


fetch_info()
