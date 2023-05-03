import requests
import fake_useragent
import bs4

headers = {
    'User-Agent': fake_useragent.UserAgent().random,
}
# to analyse the news we get

Institution_lst=['工程科学学院','科技传播系','管理学院']
titlelst = []#记录目录里所有的标题
hreflst=[]#记录目录里所有新闻链接，注意排除无效链接（http://xgyth.ustc.edu.cn
wordlst =[]#记录文字数
piclst =[]#记录图片数
news_href_lst=[]#记录每篇新闻的地址

def WordandPicCounter(web):
        pass

def PicCounter(i):
        pass

# for i in range(1,3):
#     WordCounter(i)

class Institution:
    def __init__(self, name):
        self.titlelst = []
        self.hreflst = []
    @property
    def len(self):
        return len(self.titlelst)

#-----main-----
#获取所有大标题和新闻具体链接
for i in range (0,3):
    with open(f'./catalog/{i}.html', 'r', encoding='utf-8') as f:
        content = f.read()
        soup = bs4.BeautifulSoup(content)
        hrefs = soup.find_all('a', {"target": '_blank'})
        for href in hrefs:
            hreflst.append(href.get('href'))
            titlelst.append(href.get('title'))
        # print(hreflst)
        # print(titlelst)
#---------建立每一个学院的类，包括新闻链接、标题---------
ins_class_lst = [Institution(i) for i in Institution_lst]#类
for title in titlelst:
    if not title:
        continue
    for ins in Institution_lst:
        if ins in title:
            ins_class_lst[Institution_lst.index(ins)].titlelst.append(title)#类的属性
            ins_class_lst[Institution_lst.index(ins)].hreflst.append(hreflst[titlelst.index(title)])
# print(ins_class_lst)
for i in range(0,len(hreflst)):
     if hreflst[i]!='http://xgyth.ustc.edu.cn':
        news_href_lst.append('http://stuhome.ustc.edu.cn/'+hreflst[i])
# print(news_href_lst)
# ---------------爬取所有新闻链接--------------
for i in range(0,len(news_href_lst)):
     if news_href_lst:
        resp = requests.get(news_href_lst[i], headers=headers)
        resp.encoding = 'utf-8'
        with open(f'./news/news_{i}.html', 'w+', encoding= 'utf-8') as f:
                f.write(resp.text)
# print(ins_class_lst[1].titlelst)
# print(ins_class_lst[1].hreflst)
