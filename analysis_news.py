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
#------字数统计--------
import re
for i in range (0,5):
    with open(f'./news/news_{i}.html', 'r', encoding='utf-8') as f:
        content = f.read()
        soup = bs4.BeautifulSoup(content)
#      # Count number of words
        body = soup.find('div', {'class': 'read'})
        body = str(body)
        pat = "[\u4E00-\u9FA5]+"
        lst = re.findall(pattern=pat, string=body)
        s = ''.join(lst)
        print(f'Number of Words: {len(s)}')
    # Count number of images
        num_images = len(soup.find_all('img')) - 1# minus 1 because of the logo
        print(f'Number of images: {num_images}')
        quit()
