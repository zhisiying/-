# -import re
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from lxml import etree
from bs4 import BeautifulSoup
dr = webdriver.Chrome()
dr.get('http://www.bjlzj.gov.cn/xxgk/zhbd/lzxx/')
for page in range(1, 25 + 1):
    if page == 1:
        url = 'http://www.bjlzj.gov.cn/xxgk/zhbd/lzxx/'
    else:
        url = 'http://www.bjlzj.gov.cn/xxgk/zhbd/lzxx/index_' + str(page - 1) + '.html'
    dr.get(url)
    for i in range(1, 21):
        xpath = 'html/body/div[5]/div/div[2]/dl[' + str(i) + ']/dd/a'
        dr.find_element_by_xpath(xpath).click()
        page = dr.page_source
        beau = BeautifulSoup(page, 'lxml')
        title = beau.select('h1')[0].text
        try:
            content = beau.select('div.Custom_UnionStyle')[0].get_text().replace('\n', '')
        except:
            content = beau.select('div.article_c')[0].get_text().replace('\n', '')
        print(title, content)
        dr.get(url)
