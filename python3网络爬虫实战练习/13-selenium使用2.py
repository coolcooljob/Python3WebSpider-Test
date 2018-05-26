from selenium import webdriver
import time
from selenium.webdriver import ActionChains    #动作链

#查找节点并访问页面
# browser=webdriver.Chrome()
# browser.get('http://www.taobao.com')
# lis=browser.find_elements_by_css_selector('body > div.screen-outer.clearfix > div.main > div.main-inner.clearfix > div.tbh-service.J_Module > div > ul > li:nth-child(3) > a:nth-child(1)')
# print(lis)
# browser.close()

#节点交互
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input=browser.find_element_by_id('q')
# input.send_keys('iphone')
# time.sleep(3)
# input.clear()
# input.send_keys('iPad')
# button=browser.find_element_by_class_name('btn-search')
# button.click()
# time.sleep(3)
# browser.close()

#动作链,实现一个节点的拖拽
# browser=webdriver.Chrome()
# url=''
# browser.get(url)
# browser.switch_to.frame('')
# source=browser.find_element_by_css_selector('#draggeable')
# target=browser.find_element_by_css_selector('#droppable')
# actions=ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

#执行JavaScript(比如下拉进度条)
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')    #执行下拉进度条的脚本
# browser.execute_script('alert("To Bottom")')                               #下拉到底部之后弹出一段提示
# browser.close()

#获取节点信息

#获取属性(前提是先选中这个节点)
from selenium import webdriver
from selenium.webdriver import ActionChains

# browser=webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# logo=browser.find_element_by_id('zh-top-link-logo')    #选中这个logo
# print(logo)
# print(logo.get_attribute('class'))
# browser.close()

#获取文本值
# from selenium import webdriver
#
# browser=webdriver.PhantomJS()
# browser.get('http://www.zhihu.com/explore')
# input=browser.find_element_by_class_name('zu-top-add-question')   #获取提问这个按钮，然后将此按钮的文本内容打印出来
# print(input.text)
#
# #获取ID，标签名
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

#切换frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser=webdriver.Chrome()
# url='http://www.runoob.com/try/try.php?filenanme=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')   #切换至子级Frame里面，然后尝试获取父级里面的logo,找不到的话，抛出异常
# try:
#     logo=browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No Logo!')
# browser.switch_to.parent_frame()          #切换至父级Frame里面，再次获取节点
# logo=browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
# browser.close()

#延时等待(显式等待，隐式等待)
#隐式等待,超出等待时间后，将抛出超时异常
# from selenium import  webdriver
# browser=webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('http://www.zhihu.com/explore')
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# browser.close()

#显式等待，指定要查找的节点，然后之指定一个最长等待时间，如果规定时间加载出来，就返回查找的节点，否则就抛出异常
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser=webdriver.Chrome()
# browser.get('http://www.taobao.com')
# wait=WebDriverWait(browser,10)
# input=wait.until(EC.presence_of_element_located((By.ID,'q')))   #传入条件，表示等待节点出现，下面的表示节点按钮可点击
# button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)
# browser.close()

#前进和后退(back(),forward())
# import time
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.get('http://www.baidu.com/')
# browser.get('http://www.taobao.com/')
# # browser.get('http://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


#cookies
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'job'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
# browser.close()

#选项卡操作
import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')               #新开启一个选项卡
print(browser.window_handles)                         #获取当前所有开启的选项卡的代号列表
browser.switch_to.window(browser.window_handles[1])   #切换选项卡
browser.get('https://www.taobao.com')                 #在新开启的选项卡里面打开一个网页
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])   #切回到原来的选项卡
browser.get('https://www.python.org')                 #执行操作
browser.close()