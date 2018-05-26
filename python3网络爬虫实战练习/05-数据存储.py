import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
    }
html=requests.get(url=url,headers=headers).text
doc=pq(html)
# print(doc)
items=doc('.explore-tab .feed-item').items()
print(items)
for item in items:
    question=item.find('h2').text()
    print('1')
    author=item.find('.author-link-line').text()
    answer=pq(item.find('.content').html()).text()
    with open('explore.txt','a') as f:
        f.write('\n'.join([question,author,answer]))
        f.write('\n'+'='*50+'\n')
        f.close()


# response2 = requests.get('https://p4.ssl.cdn.btime.com/t01f7081c44b722510b.jpg')
#
# with open('3.jpg','wb') as f:
#     f.write(response2.content)
#     f.close()
