import requests
from bs4 import BeautifulSoup              #利用BeautifulSoup将网页的代码按照标准的缩进打印出来
import re

# response=requests.get('http://www.baidu.com')
# response.encoding='utf-8'
# print(response.text)

# 基本用法
html=requests.get('https://www.baidu.com')
soup=BeautifulSoup(html.content,'lxml')     #注意这里的html.content,不能直接传入html
print(soup.prettify())
print(soup.title.string)

# 选择元素
print(soup.title)
print(soup.p)

# 提取信息
print(soup.title.name)    # 获取名称
print(soup.p.attrs)       # 获取属性
print(soup.p.attrs['name'])

# 获取内容
print(soup.p.string)

# 嵌套选择
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
# 子节点和子孙节点
print(soup.p.contents)   # 获取p节点的直接子节点(以列表形式返回)，即子孙节点
print(soup.p.children)   # 返回结果是生成器类型，接下来用for循环
for i,child in enumerate(soup.p.children):
    print(i,child)

print(soup.p.descendants)   # 获取子孙节点
for i,child in enumerate(soup.p.descendants):
    print(i,child)

# 父节点和祖先节点
print(soup.a.parent)     # 获取a节点的直接父节点
print(soup.a.parents)     # 获取a节点的祖先节点

# 兄弟节点
print(soup.a.next_sibling)
print(soup.a.previous_sibling)

# 提取信息
print(soup.a.next_sibling.string)
print(soup.a.previous_sibling.text)

# 方法选择器
# find_all(name,attrs,recursive,text,**kwargs)
print(soup.find_all('ul'))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))

print(soup.find_all(attrs={'name':'list-1'}))    # 返回所有匹配的元素组成的列表
print(soup.find_all(id='list-1'))

print(soup.find_all(text=re.compile('link')))

print(soup.find(name='ul'))    # 返回第一个匹配的元素

# CSS选择器
# print(soup.select('ul li'))
# print(soup.select(#list-2 .element))
# print(soup.select('.panel .panel-heading'))

# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本
for li in soup.select('li'):
    print(li.get_text())
    print(li.string)
    print(li.string)