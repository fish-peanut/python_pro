from bs4 import BeautifulSoup
import lxml

if __name__ == "__main__":
    fp = open('./test_0.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    print(soup)
