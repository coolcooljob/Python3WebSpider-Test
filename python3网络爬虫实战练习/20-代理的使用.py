#urllib
#输出结果是一个JSON，它有一个字段origin,表明了客户端的IP。
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy=''
# proxy='username:password@'     #若碰到需要认证的代理，可以进行这样的设置。
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy,
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

#requests
import requests

proxy=''
proxy='username:password@'         #有用户验证的情况
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response=requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)


#selenium(有界面：Chrome,无界面：Plantomjs)
#Chrome
from selenium import webdriver

proxy=''
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
browser=webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

#plantomjs
from selenium import webdriver

service_args=[
    '--proxy=',
    '--proxy-type=http'
]
# service_args=[
#     '--proxy=127.0.0.1:9743',
#     '--proxy-type=http',
#     '--proxy-auth=username:password'
# ]        #需要进行认证设置的时候
browser=webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)