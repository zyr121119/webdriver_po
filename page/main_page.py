from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID,"menu_contacts").click()
        #self.driver.find_element(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)