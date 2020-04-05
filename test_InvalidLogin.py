import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from selenium import webdriver
from NewProject.TestUtility.xlutiles import xlUtiles
from NewProject.TestUtility.CaptureScreenShot import SS
import logging
from datetime import datetime
from NewProject.PageLayer.test_Locators import Locator
from NewProject.PageLayer.test_loginPage import test_loginPage
from selenium.webdriver import ActionChains
import unittest
import HtmlTestRunner

logging.basicConfig(filename="C:/Users/junaid/PycharmProjects/Demo/NewProject/TestLog/Info.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
logging.info("Valid Login")
logging.info("__________________________________")
logging.info(datetime.today())
class test_MercuryLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_validLogin(self):
        ss_path = "/ScreenShot/"
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        ss = SS(driver)

        path = ("C:/Users/junaid/PycharmProjects/Demo/NewProject/TestData/Login.xlsx")
        rows = xlUtiles.getRowCount(path,'Sheet1')
        logging.info("Login Page Loaded Successfully")
        for r in range (2,rows+1):
            UserName = xlUtiles.readData(path,'Sheet1',r,1)
            PassWord = xlUtiles.readData(path,'Sheet1',r,2)

            ss.ScreenShot(ss_path)
            ss.ScreenShot("Loginpage.png")

            self.driver.find_element_by_xpath("//tr//tr//tr//tr//tr[2]//td[2]//input[1]").send_keys(UserName)
            logging.info("Entered User Name as : "+ UserName)
            self.driver.find_element_by_xpath("//*[@name='password']").send_keys(PassWord)
            logging.info("Entered Pass Word as : " + PassWord)
            ss.ScreenShot("LoginDetail.png")
            self.driver.find_element_by_name("login").click()
            logging.info("Clicked on Login Button")

            if driver.title == "Find a Flight: Mercury Tours:":
                print("Test case pass")
                xlUtiles.writeData(path, "Sheet1", r, 3, "Test Pass")
                ss.ScreenShot("Detailpage.png")
                logging.info("Mercury Tours Page Displayed ")
            else:
                print("Test case Fail")
                xlUtiles.writeData(path, "Sheet1", r, 3, "Test Failed")
                logging.info("Mercury Tours Page Not Displayed")


    @classmethod
    def tearDownClass(cls):
        cls.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
        logging.info("Click On Sin Off Link")
        cls.driver.close()
        cls.driver.quit()
        logging.info("Browser Close successfully")
if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/junaid/PycharmProjects/Demo/NewProject/TestReport/HtmlReport'))

#  C:\Users\junaid\PycharmProjects\Demo\NewProject>python -m TestLayer.test_InvalidLogin
