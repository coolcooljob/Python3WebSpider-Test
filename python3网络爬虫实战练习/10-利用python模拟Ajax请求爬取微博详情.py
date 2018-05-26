import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

client=MongoClient()        #连接moongodb数据库，定义一些需要用到的变量
db=client['weibo']
collection=db['weibo']

base_url=''
headers={
    'Host: m.weibo.cn',
    'Referer: https://m.weibo.cn/',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
    'X-Requested-With: XMLHttpRequest'
    }

def get_page(page):               #定义一个获取ajax请求内容的函数，结果返回json数据格式
    params={
        'type':'uid',
        'value':'',
        'contained':'',
        'page':page
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):      #解析返回的json数据，并返回一个字典，包括微博的id，正文，赞数，评论数以及转发数
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get()
            weibo['text']=pq(item.get('text')).text()        #借助pquery将正文中的html去掉
            weibo['attitudes']=item.get('attitudes_count')
            weibo['comments']=item.get('comments_count')
            weibo['reposts']=item.get('reposts_count')
            yield weibo

def save_to_mongo(result):       #定义一个将数据存到mongodb数据库的方法
    if collection.insert(result):
        print('Save to Mongo!')

if __name__=='__main__':
    for page in range(1,11):        #遍历一下page，一共10页，将提取到的结果打印出来
        json=get_page(page)
        results=parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)