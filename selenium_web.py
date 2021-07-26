from selenium import webdriver


class infow:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

    def speakable(self):
        read = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
        return read


if __name__ == '__main__':
    infow().speakable()
