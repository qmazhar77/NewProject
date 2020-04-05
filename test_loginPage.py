from NewProject.PageLayer.test_Locators import Locator

class test_loginPage():

    def __(self,driver):
        self.driver = driver

        self.username_text_name = Locator.username_text_name
        self.password_text_name = Locator.password_text_name
        self.login_button_name = Locator.login_button_name

    def enter_username(self,UserName):
        self.driver.find_element_by_name(self.username_text_name).clear()
        self.driver.find_element_by_name(self.username_text_name).send_keys(UserName)

    def enter_password(self,PassWord):
        self.driver.find_element_by_name(self.password_text_name).clear()
        self.driver.find_element_by_name(self.password_text_name).send_keys(PassWord)

    def click_Login_button(self):
        self.driver.find_element_by_name(self.login_button_name).click()

