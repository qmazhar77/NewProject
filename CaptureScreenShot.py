from _datetime import datetime

class SS:
    def __init__(self,driver):
        self.driver = driver

    def ScreenShot(self, path):
        filepath = "C:/Users/junaid/PycharmProjects/Demo/NewProject/TestReport/ScreenShot/"
        currentTime = datetime.now()
        pictime = currentTime.strftime("%Y_%m_%d-%H_%M_%S")
        picName = pictime + '.png'
        completefilepath = filepath + picName
        self.driver.save_screenshot(completefilepath)