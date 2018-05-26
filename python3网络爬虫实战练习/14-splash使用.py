import requests


#利用render.html获取经过JavaScript渲染之后的页面与源代码
'curl http://localhost:8050/render.html?url=https://www.baidu.com'



#利用render.har获取页面加载的HAR数据，返回的是json数据
'curl http://localhost:8050/render.har?url=https://www.jd.com&wait=5'



#获取京东首页渲染完成之后的页面截图，并将其保存在本地（调用了splash的API render.png）
url='http://localhost:8050/render.png?url=https://www,jd.com&wait=5&width=1000&height=700'
response=requests.get(url)
with open('taobao.png','wb') as f:
    f.write(response.content)



#此接口包含前面借口的所有功能，返回json数据格式render.json
'curl http://localhost:8050/render.json?url=https://httpbin.org'



#此接口用于实现与Splash Lua脚本的对接（execute）
#先实现一个Lua一个最简单的脚本
# function main(splash)
#     return 'Hello'
# end
#然后将此脚本转化为URL编码的字符串，拼接到execute接口后面
'curl http://localhost:8050/execute?lua_source=function+main(.*?)end'
#运行结果，输出Hello,利用python实现
import requests
from urllib.parse import quote
lua='''
    function main(splash)
    return 'Hello'
end
'''
url='http://localhost:8050/execucte?lua_source='+quote(lua)
response=requests.get(url)
print(response.text)