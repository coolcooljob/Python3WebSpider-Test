from pyquery import PyQuery as pq
import requests

# URL初始化
doc=pq(url='https://www.cuiqingcai.com')    #请求url，得到结果
doc=pq(requests.get('https://www.cuiqingcai.com').text)   #等价于上面那句
print(doc('title'))

# 文件初始化
doc=pq(filename=demo.html)
print(doc('li'))

# 基本CSS选择器
html='''

'''
doc=pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 查找节点
# 子节点
html='''

'''
doc=pq(html)
items=doc('.list')
print(type(items))
print(items)
lis=items.find('li')     # 查找所有的子孙节点
# lis=items.children()     # 查找所有的子节点
# lis=items.children('.active')    # 查找字节点中class为active的节点
print(type(lis))
print(lis)


# 父节点
doc=pq(html)
items=doc('.list')
container=items.parent()    # 查找父节点
# container=items.parents()   # 查找祖先节点
print(type(container))
print(container)

# # 兄弟节点
doc=pq(html)
li=doc('.list .item-0.active')    # 选取class为list的节点内部class为item-0和active的节点
print(li.siblings())        # 查找兄弟节点


# 遍历(多个节点)，调用items方法
doc=pq(html)
lis=doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))

# 获取信息
# 获取属性
doc=pq(html)
a=doc('.item-0.active')
print(a,type(a))
print(a.attr('href'))      # 与下面等价
# print(a.attr.hrer())

# 获取多个属性，需要遍历才能实现
doc=pq(html)
a=doc('a')
for i in a.items():
    print(a.attr('href'))

# 获取文本(调用text()方法实现)
doc=pq(html)
a=doc('.item-0.active a')
print(a)
print(a.text())    # 去掉节点的包括的所有HTML，只返回纯文字内容

# 获取HTML内容
doc=pq(html)
li=doc('.item-0.active')
print(li)
print(li.html)

# 如果选取的是多个节点，text()或html()返回的是第一个li节点的内部的HTML文本，而text()返回的是所有的li节点内部的纯文本

# 节点操作,比如为某个节点移除或者增添一个class
doc=pq(html)
li=doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')

# attr,text和html(改变属性，文本，以及html)
doc=pq(html)
li=doc('.item-0.active')
li.attr('name','link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)


# remove()
# wrap.find('p').remove()
# print(wrip.text())

# 伪类选择器



