import fake_useragent
import bs4
import re
headers = {
    'User-Agent': fake_useragent.UserAgent().random,
}
# to analyse the news we get

Institution_lst = ['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理','化学','马克思主义','金融','科技传播','微尺度','人文','数学','天文','网络空间安全']
titlelst = []#Record all the headings in the directory
hreflst=[]#记Keep a record of all news links in the directory, taking care to exclude invalid links (http://xgyth.ustc.edu.cn
wordlst =[]#Record the number of words
piclst =[]#Record the number of pictures
news_href_lst=[]#Record the network address of each news article

#------count the words--------
def Counter(web):
        with open(web, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = bs4.BeautifulSoup(content)
    #      # Count number of words
            body = soup.find('div', {'class': 'read'})
            body = str(body)
            pat = "[\u4E00-\u9FA5]+"
            lst = re.findall(pattern=pat, string=body)
            num_words = ''.join(lst)
            # print(f'Number of Words: {len(num_words)}')
        # Count number of images
            num_images = len(soup.find_all('img')) - 1# minus 1 because of the logo
            # print(f'Number of images: {num_images}')
            return len(num_words),num_images
if __name__ == '__main__':       
    for i in range (0,5):
        Counter(f'./news/news_{i}.html')