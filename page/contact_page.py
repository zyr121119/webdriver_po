from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class ContactPage(BasePage):
    def goto_add_department(self):
        sleep(3)
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()

        # self.driver.find_element_by_class_name("member_colLeft_top_addBtn").click()
        # self.driver.find_element_by_class_name("js_create_party").click()
        from page.add_department_page import AddDepartment
        return AddDepartment(self.driver)
    def get_department_list(self):
        sleep(5)
        departments=self.find_elements(By.CSS_SELECTOR,".jstree-anchor")
        department=[]
        for depart in departments:
            print(depart.text)
            department.append(depart.text)
        return department
    def get_tips(self):
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        text1=self.find(By.ID,"js_tips").text
        return text1