import requests
import fake_useragent
import bs4
from analysis_news import Counter
import pandas as pd

headers = {
    'User-Agent': fake_useragent.UserAgent().random,
}
# to analyse the news we get
Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
titlelst = []#Record all the headings in the directory
hreflst=[]#Keep a record of all news links in the directory, taking care to exclude invalid links (http://xgyth.ustc.edu.cn
wordlst =[]#Record the number of words
piclst =[]#Record the number of pictures
news_href_lst=[]#Keep a record of all news links in the directory
paylst=[]#Record the fee
class Institution:
    def __init__(self, name):
        self.name = name
        self.titlelst = []
        self.hreflst = []
        self.timelst= []
        self.paylst= []
    @property
    def len(self):
        return len(self.titlelst)
    
    def save(self):
        df = pd.DataFrame({'title':self.titlelst,'href':self.hreflst,'time':self.timelst,'pay': self.paylst})
        df.to_csv(f'./data_ins/{self.name}.csv', encoding='utf-8')

    def read_data(self):
        df = pd.read_csv(f'./data_ins/{self.name}.csv')
        return df

#-----main-----
if __name__ == '__main__': 
#Get specific links to all headlines and news
    for i in range (0,100):
        with open(f'./catalog/{i}.html', 'r', encoding='utf-8') as f:
            content = f.read()
            soup = bs4.BeautifulSoup(content)
            hrefs = soup.find_all('a', {"target": '_blank'})
            times = soup.find_all('span',{"class": 'news_meta'})
            for href in hrefs:
                hreflst.append(href.get('href'))
                titlelst.append(href.get('title'))
                time = str(href.get('href')) 
                timelst.append(time[1:10])
            # print(hreflst)
            # print(len(hreflst))
            # print(titlelst[10])
            # print(timelst)
            # print(len(timelst))

    for i in range(0,len(hreflst)):
        if hreflst[i]!='http://xgyth.ustc.edu.cn':
            news_href_lst.append('http://stuhome.ustc.edu.cn/'+hreflst[i])

    # print(len(news_href_lst))

    # ---------------Crawl all news links--------------
    for i in range(0,len(news_href_lst)):
         if news_href_lst:
            resp = requests.get(news_href_lst[i], headers=headers)
            print (resp.status_code)
            resp.encoding = 'utf-8'
            with open(f'./news/news_{i}.html', 'w+', encoding= 'utf-8') as f:
                f.write(resp.text)
    # -----Calculate the manuscript fee
    # print(len(news_href_lst))
    for i in range(0,len(news_href_lst)-1):
        num_word,num_pic=Counter(f'./news/news_{i}.html')
        pay = 30 
        if num_word > 800:
            pay+=20
        if num_pic > 4:
            pay+=20
        if (i+14)%14 == 0.0:
            paylst.append(0) 
        paylst.append(pay)


    #---------Establish each college class, including news links, headlines---------
    ins_class_lst = [Institution(i) for i in Institution_lst]#类
    for title in titlelst:
        if not title:
            continue
        for ins in Institution_lst:
            if ins in title:
                ins_class_lst[Institution_lst.index(ins)].titlelst.append(title)#类的属性
                ins_class_lst[Institution_lst.index(ins)].hreflst.append(hreflst[titlelst.index(title)])
                ins_class_lst[Institution_lst.index(ins)].timelst.append(timelst[titlelst.index(title)])
                ins_class_lst[Institution_lst.index(ins)].paylst.append(paylst[titlelst.index(title)])

        ins_class_lst[29].save()