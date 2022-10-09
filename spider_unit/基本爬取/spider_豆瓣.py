import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"

    param = {
        "type": "24",
        "interval_id": "100:90",
        "action": "",
        "start": "0",
        "limit": "20"
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
    }

    response = requests.get(url=url, params=param, headers=headers)

    movie_page = response.json()

    with open("./豆瓣喜剧电影排行榜.json", "w", encoding='utf-8') as fp:
        json.dump(movie_page, fp=fp, ensure_ascii=False)

    print('got it!!')

