import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.114 Safari/537.36 Edg/103.;0.1264.49 "
    }

urls = [
    "https://www.bilibili.com/",
    "https://www.baidu.com/",
    "https://www.douban.com/"
]


def get_content(url):
    print("正在爬取:", url)
    # get方法是一个阻塞的方法
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print("长度为:", len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
