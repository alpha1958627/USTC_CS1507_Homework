import requests
import fake_useragent
import bs4

# to get the news we need

headers = {
    'User-Agent': fake_useragent.UserAgent().random,
}
href_list = [f'http://stuhome.ustc.edu.cn/2314/list{i}.htm' for i in range(1, 101)]


#get the title and href

def Getnewsoutline(i):
        if i == 0:
            resp = requests.get('http://stuhome.ustc.edu.cn/2314/list.htm', headers=headers)
            resp.encoding = 'utf-8'
            with open(f'./catalog/0.html', 'w+', encoding= 'utf-8') as f:
                f.write(resp.text)
        else:
            resp = requests.get(href_list[i], headers=headers)
            resp.encoding = 'utf-8'
            with open(f'./catalog/{i}.html', 'w+', encoding= 'utf-8') as f:
                f.write(resp.text)

def Getnews(i):
     pass
#get 

# resp = requests.get(f'http://stuhome.ustc.edu.cn/2314/list100.htm', headers=headers)
# resp.encoding = 'utf-8'
# with open('100.html', 'w+', encoding= 'utf-8') as f:
#         f.write(resp.text)

for i in range (0,100):
    Getnewsoutline(i)

