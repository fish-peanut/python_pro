import requests

if __name__ == "__main__":
    title = input("enter a word : ")
    url = f"https://www.sogou.com/web"

    param = {
        "query": title
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
    }
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    print(page_text)

    with open(f"./sogou__{title}.html", 'w', encoding='utf-8') as file_web:
        file_web.write(page_text)

    print("got it!")
