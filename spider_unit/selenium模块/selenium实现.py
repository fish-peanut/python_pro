from selenium import webdriver
from lxml import etree
from time import sleep


bro = webdriver.Chrome(executable_path='')

bro.get('https://www.baidu.com/')

# page_source获取页面源码数据
page_text = bro.page_source

tree = etree.HTML(page_text)

li_list = tree.xpath('')

sleep(2)
bro.quit()


# 后面包括自动化操作啥的以后有空写。。。。
