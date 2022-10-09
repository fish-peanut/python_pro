import requests
import json

if __name__ == "__main__":
    def weblistnum():
        page_text = response.text
        webdata = json.loads(page_text)
        nump = webdata['Table'][0]['rowcount']
        return nump//10 + (nump % 10 > 0)
    limitnum = i = 1
    position = input()
    while True:
        url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
        }

        data = {
            "cname": "",
            "pid": "",
            "keyword": position,
            "pageIndex": i,
            "pageSize": 10
        }

        response = requests.post(url=url, data=data, headers=headers)

        page = response.json()

        if 1 == i:
            limitnum = weblistnum()

        fp = open("kfc_restaurant_position.json", "a", encoding='utf-8')
        json.dump(page, fp=fp, ensure_ascii=False)
        fp.close()
        if limitnum == i:
            break
        i += 1
    print("got it!!")
