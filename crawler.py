import requests
import fake_useragent

# to get the news we need

headers = {
    'User-Agent': fake_useragent.UserAgent().random,
}
href_list = [f'http://stuhome.ustc.edu.cn/2314/list{i}.htm' for i in range(1, 101)]
for i in range (1,101):
    resp = requests.get(href_list[i], headers=headers)
    resp.encoding = 'utf-8'
    with open(f'{i}.html', 'w+', encoding= 'utf-8') as f:
        f.write(resp.text)

# resp = requests.get(f'http://stuhome.ustc.edu.cn/2314/list100.htm', headers=headers)
# resp.encoding = 'utf-8'
# with open('100.html', 'w+', encoding= 'utf-8') as f:
#         f.write(resp.text)