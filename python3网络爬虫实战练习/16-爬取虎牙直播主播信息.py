import requests
from pyquery import PyQuery as pq


url='http://www.huya.com/g/wzry'
def get_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
            # print(response.text)
        return None
    except ConnectionError:
        get_page(url)

def parse_page(html):
    doc=pq(html)
    items=doc('.js-responded .mod-list .box-bd .live-list .game-live-list').items()
    for item in items:
        if item:
            info={
                'href':item.find('.tag-right').attr('href'),
                'title':item.find('.tag-right').attr('title').text(),
                'image':item.find('.img .pic').attr('src'),
                'num':item.find('.txt .num .js-num').text()
            }
            print(info)
        else:
            return None




def main():
    html=get_page(url)
    print(html)
    parse_page(html)
    print(parse_page(html))

if __name__=='__main__':
    main()