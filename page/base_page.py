import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver:webdriver=None):
        #self.driver=webdriver.Chrome()
        if driver is None:
            self.driver=webdriver.Chrome()
            self._login()
        else:
            self.driver=driver
        self.driver.implicitly_wait(5)

    def find(self,path,name):
        return  self.driver.find_element(path,name)

    def find_elements(self,path,name):
        return  self.driver.find_elements(path,name)

    def _login(self):
        try:
            self.driver.get("https://work.weixin.qq.com/")
            with open("../testcases/cookie.json","r")as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            text=self.driver.find_element(By.XPATH,"//*[@id='menu_index']").text
            if text=="首页":
                print("cookie 正确")
            else:
                raise Exception
        except Exception as e:
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
            sleep(10)
            print("cookie 不正确,请扫码登录")

            #WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(By.XPATH,"//*[@id=menu_index]"))
            cookies=self.driver.get_cookies()
            with open("cookie.json","w") as f:
                json.dump(cookies,f)

