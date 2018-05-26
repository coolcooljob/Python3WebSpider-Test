from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#通过selenium来驱动浏览器加载网页的话，可以直接拿到JavaScript渲染的结果了，不用担心使用的是什么加密结果
browser=webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    # input_=browser.find_elements_by_id('kw')
    # input_.send_keys('Python')
    # input_.send_keys(Keys.ENTER)
    # wait=WebDriverWait(browser,10)
    # wait.until(EC.presence_of_element_located((By.ID,'content-left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


