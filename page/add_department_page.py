from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage

class AddDepartment(BasePage):
    def add_department(self,name):
        # windows=self.driver.window_handles
        # print(windows)
        # self.driver.switch_to_window(windows[-1])
        sleep(5)
        self.find(By.NAME,"name").send_keys(name)
        self.find(By.CLASS_NAME,"js_parent_party_name").click()
        self.find(By.CSS_SELECTOR,"#__dialog__MNDialog__ > div [id='1688850100228413_anchor']").click()
        self.find(By.CSS_SELECTOR,"#__dialog__MNDialog__ > div > div:nth-child(3) > a:nth-child(1)").click()
        from page.contact_page import ContactPage
        return ContactPage(self.driver)