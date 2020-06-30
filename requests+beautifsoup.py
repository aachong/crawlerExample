import requests
from bs4 import BeautifulSoup


def getContent(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    }
    return requests.get(url, headers=headers).text


content = getContent('https://cn.element14.com/')
content
soup = BeautifulSoup(content, 'html.parser')

# 获取html的标签
tag = soup.article.div.ul.li
# 属性只能获取到第一个tag，若想获取到所有的 li 标签，可以通过 find_all() 方法
ls = soup.article.div.ul.find_all('li')
tag = soup.title
tag
# 查看获取部分的标签
tag.name
# 查看获取部分的内容
tag.string

catalogue = soup.find_all('li',role= 'menuitem')
for i in catalogue:
    if i.string!=None:
        print(i.string)

for i in catalogue:
    try:
        print(i.a.string)
    except:
        pass

