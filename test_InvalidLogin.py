from selenium import webdriver
#from NewProject.TestUtility.xlutiles import xlUtiles
from NewProject.TestUtility.test_CaptureScreenShot import test_SS
from selenium.webdriver.support.ui import Select
import logging
import unittest
import HtmlTestRunner
from datetime import datetime
import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from NewProject.PageLayer.test_Locators import Locator
from NewProject.PageLayer.test_loginPage import test_loginPage
from selenium.webdriver import ActionChains


logging.basicConfig(filename="C:/Users/junaid/PycharmProjects/Demo/NewProject/TestLog/Info.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
logging.info("-------------------------------------")
logging.info("Valid Login")
logging.info("-------------------------------------")
logging.info(datetime.today())

class test_MercuryLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_001validLogin(self):
        ss_path = "/ScreenShot/"
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        ss = test_SS(driver)
        #path = ("C:/Users/junaid/PycharmProjects/Demo/NewProject/TestData/Login.xlsx")
        #rows = xlUtiles.getRowCount(path,'Sheet1')
        logging.info("Login Page Loaded Successfully")

        #for r in range (2,rows+1):
        #    username = xlUtiles.readData(path,'Sheet1',r,1)
        #    password = xlUtiles.readData(path,'Sheet1',r,2)

        ss.ScreenShot(ss_path)
        ss.ScreenShot("Loginpage.png")

        driver.find_element_by_xpath("//*[@type='text' and @name='userName']").send_keys("mercury")
        logging.info("Entered User Name as : ")
        driver.find_element_by_xpath("//*[@type='password' and @name='password']").send_keys("mercury")

        logging.info("Entered Pass Word as : ")
        ss.ScreenShot("LoginDetail.png")
        driver.find_element_by_name("login").click()
        logging.info("Clicked on Login Button")

        #except Exception as e:

        if driver.title == "Find a Flight: Mercury Tours:":
            print("Test case pass")
        #    xlUtiles.writeData(path, "Sheet1", r, 3, "Test Pass")
            ss.ScreenShot("Detailpage.png")
            logging.info("Mercury Tours Page Displayed ")
        else:
            print("Test case Fail")
        #    xlUtiles.writeData(path, "Sheet1", r, 3, "Test Failed")
            logging.info("Mercury Tours Page Not Displayed")
            driver.close()

    def test_002flight_search(self):
        logging.info("-------------------------------------")
        logging.info("Flight Serach")
        logging.info("-------------------------------------")
        driver = webdriver.Chrome()
        driver.get("http://newtours.demoaut.com/")
        driver.maximize_window()
        logging.info("Login Page Loaded Successfully")
        driver.find_element_by_xpath("//*[@type='text' and @name='userName']").send_keys("mercury")
        logging.info("Enter User Name")
        driver.find_element_by_xpath("//*[@type='password' and @name='password']").send_keys("mercury")
        logging.info("Enter Pass Ward")
        # driver.find_element_by_name("userName").send_keys("mercury")
        # driver.find_element_by_name("password").send_keys("mercury")
        driver.find_element_by_xpath("//*[@type='image' and @value='Login']").click()
        logging.info("Click On Login Button")

        # select radio by CSS-Selector
        driver.find_element_by_css_selector("input[type='radio'][value='oneway']").click()
        logging.info("Select One Way Radio Button")

        passerger_element = driver.find_element_by_name("passCount")
        passenger_drp = Select(passerger_element)
        # select value by visible test
        passenger_drp.select_by_visible_text("2")
        logging.info("Select 2 Option From Drop Down")

        from_element = driver.find_element_by_name("fromPort")
        from_drp = Select(from_element)
        from_drp.select_by_index(3)
        logging.info("Select New York Option From Drop Down")

        month_element = driver.find_element_by_name("fromMonth")
        month_drp = Select(month_element)
        month_drp.select_by_value("3")
        logging.info("Select April Month Option From Drop Down")

        day_element = driver.find_element_by_name("fromDay")
        day_drp = Select(day_element)
        day_drp.select_by_visible_text("10")
        logging.info("Select 10 Option From Drop Down")

        to_element = driver.find_element_by_name("toPort")
        to_drp = Select(to_element)
        to_drp.select_by_value("Frankfurt")
        logging.info("Select Frankfurt Option From Drop Down")

        tMonth_element = driver.find_element_by_name("toMonth")
        tmonth_drp = Select(tMonth_element)
        tmonth_drp.select_by_index(5)
        logging.info("Select June Option From Drop Down")

        today_element = driver.find_element_by_name("toDay")
        today_drp = Select(today_element)
        today_drp.select_by_index(7)
        logging.info("Select 8 Option From Drop Down")

        driver.find_element_by_xpath("//*[@type='radio' and @value='Business']").click()
        logging.info("Select Business Class Radio Button")

        airline_element = driver.find_element_by_name("airline")
        airline_drp = Select(airline_element)
        airline_drp.select_by_index(2)
        logging.info("Select Unified AirLines Option From Drop Down")

        driver.find_element_by_name("findFlights").click()
        logging.info("Click on Continue Button")

        if driver.title == "Select a Flight: Mercury Tours":
            print("Test case pass")
            logging.info("Select a Flight Mercury Tours Page Displayed ")
        else:
            print("Test case Fail")
        #    xlUtiles.writeData(path, "Sheet1", r, 3, "Test Failed")
            logging.info("Select a Flight Mercury Tours Page Not Displayed")
            driver.close()


        #singoff = driver.find_element_by_link_text("SIGN-OFF")
        #action = ActionChains(driver)
        #action.move_to_element(singoff).click().perform()



    @classmethod
    def tearDownClass(cls):
        cls.driver.find_element_by_link_text("SIGN-OFF").click()
        logging.info("Click On Sin Off Link")
        #cls.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/junaid/PycharmProjects/Demo/NewProject/TestReport/HtmlReport'))

#  C:\Users\junaid\PycharmProjects\Demo\NewProject>python -m TestLayer.test_InvalidLogin
# C:\Users\junaid\PycharmProjects\Demo\NewProject>pytest -v -s test_InvalidLogin.py

# for execution in parallel full path of the folder and the "py.test -n 2"