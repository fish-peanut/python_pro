from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    url = "http://guoxue.lishichunqiu.com/gdxs/sanguoyanyi/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69 "
    }

    response = requests.get(url=url, headers=headers)
    request_page_text = response.text

    soup = BeautifulSoup(request_page_text, 'lxml')
    # name_list = soup.findAll("table", class_="line_bottom")
    name_card_list = soup.select(".line_bottom  a")
    fp = open('./三国演义.text', 'w', encoding='utf-8')
    for card in name_card_list:
        page_name = card.get_text()
        page_html = card['href']
        every_page_html = requests.get(url=page_html, headers=headers).text
        every_page_soup = BeautifulSoup(every_page_html, 'lxml')
        every_page = every_page_soup.find('div', id="content")
        page_detail = every_page.text
        print(page_name+'爬取完毕！！！\n')
        fp.write(page_name+'\n'+page_detail+'\n')
    fp.close()
    print("over!!!")
