import requests
import re
import os

if __name__ == "__main__":
    if not os.path.exists('./搞笑段子'):
        os.mkdir('./搞笑段子')
    url = "https://www.diyifanwen.com/tool/duanzi/911093.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
    }

    ex = '<p>(.*?)</p>'

    page_html = requests.get(url=url, headers=headers)

    page_html.encoding = 'GB2312'

    page_text = page_html.text
    print(page_text)

    result_list = re.findall(ex, page_text, re.M)

    with open('./搞笑段子/段子.text', 'w', encoding='utf-8') as fp:
        for data in result_list:
            data = data.replace(u'\u3000', u"")
            fp.write(data)
            fp.write('\n')

    print("over ! ! !")

