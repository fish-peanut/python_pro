import requests
import json

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"

    words = input("请输入您要翻译的单词 : ")

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
    }
    data = {
        "kw": words
    }
    response = requests.post(url=url, data=data, headers=headers)

    page = response.json()

    fileName = words+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(page, fp=fp, ensure_ascii=False)
    fp.close()

    print('got it!')
