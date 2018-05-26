import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
from redis import StrictRedis


redis=StrictRedis(host='localhost',port=6379,db=0,password=None)

def get_one_page(offset):      #实现方法来加载单个Ajax请求的结果，返回json的字符串格式
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        return None

def get_images(json):       #实现一个解析方法，提取每条数据的image_list字段中的每一张图片的链接，将图片链接和图片所属的标题一并返回，可以构造一个生成器
    if json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list')
            if images:
                for image in images:
                    yield{
                        'image':'http:'+image.get('url'),
                        'title':title,
                    }
            else:
                return None
#定义一个保存图片的方法，首先根据item的title来创建文件夹，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写
#入文件。图片的名称可以使用其内容的MD5值，这样可以去除重复。
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}{2}'.format(item.get('title'),md5(response.content).hexdigest(),'.jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
        # save_to_redis(f)
    except requests.ConnectionError:
        print('Failed to Save Image!')
    except requests.exceptions.MissingSchema as rem:
        print(rem)

# def save_to_redis(f):       #定义一个将数据存到mongodb数据库的方法
#     if redis.insert(f):
#         print('Save to Redid!')


def main(offset):
    json=get_one_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START=1
GROUP_END=20
if __name__=='__main__':
    pool=Pool()
    groups=([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)        #利用多线程的线程池，调用其map方法实现多线程下载
    pool.close()
    pool.join()

