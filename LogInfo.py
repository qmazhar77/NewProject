import logging

class Log:
    def __init__(self,driver):
        self.driver = driver

    def LogInfo(self, path):
        logging.basicConfig(filename="C:/Users/junaid/PycharmProjects/Demo/NewProject/TestLog/Info.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )