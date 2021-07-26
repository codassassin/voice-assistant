from selenium import webdriver


class returnXPath:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

    def returnRead(self, xPath):
        read = self.driver.find_element_by_xpath(xPath)
        return read


if __name__ == '__main__':
    returnXPath().returnRead()
