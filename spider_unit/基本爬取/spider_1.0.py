import requests

title = input()
print(title)

if __name__ == "__main__":
    url = f'https://www.sogou.com/web?query={title}'
    response = requests.get(url=url)

    page_text = response.text

    print(page_text)

    with open(f'./sogou _ {title}.html', "w", encoding='utf-8') as file_p:
        file_p.write(page_text)

    print("爬取数据结束")
