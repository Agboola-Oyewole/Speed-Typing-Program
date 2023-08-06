from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RandomWords:
    def __init__(self):
        self.chrome_path = "C:/Development/chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.get(url='https://www.randomlists.com/random-words?dup=false&qty=50')
        time.sleep(2)
        self.lists = self.driver.find_elements(By.CSS_SELECTOR, 'ol li')
        self.random_words = [item.text for item in self.lists]
        self.driver.quit()

