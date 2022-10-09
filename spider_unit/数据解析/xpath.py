from lxml import etree
import requests

url = ''
headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
    }
response = requests.get(url=url, headers=headers).text
tree = etree.HTML(response)
list_link = tree.xpath('')

print(list_link)
i = 70
for li in list_link:
    fp = open(f'../pic{i}', 'wb')
    a = requests.get(url=li, headers=headers).content
    fp.write(a)
    fp.close()
    i = i+1
    if i == 90:
        break
print('over!!!')
