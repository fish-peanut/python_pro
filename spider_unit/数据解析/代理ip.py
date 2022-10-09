import requests

# url = "https://www.baidu.com/s?wd=ip"
url = "http://httpbin.org/get"
# url = "https://ip.hao86.com/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.114 Safari/537.36 Edg/103.;0.1264.49 "
    }
proxices = {
    "http": "http://222.92.207.98:40080",
    "https": "https://222.92.207.98:40080"
}
ip_page = requests.get(url=url, headers=headers, proxies=proxices)
print(ip_page.text)

# with open("./ip页面.html", "w", encoding='utf-8') as fp:
#     fp.write(ip_page)

