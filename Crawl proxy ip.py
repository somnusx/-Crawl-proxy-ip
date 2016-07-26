import requests
from bs4 import BeautifulSoup
from lxml import etree


httphead = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'http://www.xicidaili.com/'

r = requests.get(url, headers=httphead)

html = r.text

soup = BeautifulSoup(html, 'html.parser', from_encoding='utf8')

r = soup.find_all('tr', class_='odd')

result = []

for ht in r:
    html = etree.HTML(str(ht))
    res = html.xpath('//td[2]/text()|//td[3]/text()')
    rst = res[0] + ":" + res[1]
    result.append(rst)
    print(res)
    
print(result)
