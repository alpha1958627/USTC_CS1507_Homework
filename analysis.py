import bs4

# to analyse the news we get

for i in range(1,3):
    with open(f'./news/{i}.html', 'r', encoding='utf-8') as f:
        content = f.read()
        soup = bs4.BeautifulSoup(content)
    hrefs = soup.find_all('a', {"target": '_blank'})
    for href in hrefs:
        print(href.get('href'))
        print(href.get('title'))

