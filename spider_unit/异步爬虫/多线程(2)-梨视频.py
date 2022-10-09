from multiprocessing.dummy import Pool
import random
from lxml import etree
import requests
import time

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.114 Safari/537.36 Edg/103.;0.1264.49 ",
    }

base_url = "https://www.pearvideo.com/"
main_link = base_url+'category_5'  # 主页url

response = requests.get(url=main_link, headers=headers).text
tree = etree.HTML(response)

# 分离出各个视频页面的url和视频标题。
urls = []
li_element = tree.xpath('//*[@id="listvideoListUl"]//div/a[@class="vervideo-lilink actplay"]')
for element in li_element:
    # 获取视频名称。
    name = element.xpath('.//div[@class="vervideo-title"]/text()')[0] + '.mp4'
    # 获取视频ajax请求的真实地址。
    url_id = element.xpath('./@href')[0].replace('video_', '')
    base_video_jsp_link = 'https://www.pearvideo.com/videoStatus.jsp?'
    param = {
        'contId': url_id,
        'mrd': str(random.random())
    }
    # 发送ajax请求,获取响应数据
    # 此处headers需封装referer,否则爬取失败
    headers["Referer"] = "https://www.pearvideo.com/" + 'video_' + url_id
    # 分离出MP4的伪url
    detail_page = requests.get(url=base_video_jsp_link, params=param, headers=headers).json()
    # 此时获取到的是伪url,需对其替换部分内容
    mp4_url = detail_page['videoInfo']['videos']['srcUrl']
    # "https://video.pearvideo.com/mp4/third/20220714/1658055640770-12033417-191233-hd.mp4"
    # 替换内容获取真正的url
    mp4_url_list = mp4_url.split('/')
    change_list = mp4_url_list[-1].split('-')
    change_list[0] = 'cont-' + url_id
    mp4_url_list[-1] = '-'.join(change_list)
    mp4_url = '/'.join(mp4_url_list)
    # 建立字典方便存储。
    video_dic = {
        'name': name,
        'url': mp4_url
    }
    # 加入到要爬取的队列中。
    urls.append(video_dic)
    # 删除不再使用的Referer
    headers.pop('Referer')


# 获取各个视频的详细数据。
def get_video_data(video_dic):
    print(video_dic['name']+'正在下载中.........')
    video_data = requests.get(url=video_dic['url'], headers=headers).content
    with open(video_dic['name'], 'wb') as fp:
        fp.write(video_data)
    print(video_dic['name'] + '下载成功!')


start_time = time.time()
pool = Pool(4)
pool.map(get_video_data, urls)
pool.close()
pool.join()
end_time = time.time()
print('%d seconds' % (end_time - start_time))
