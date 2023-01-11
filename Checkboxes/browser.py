
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Browser:

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/checkbox")
    driver.maximize_window()
    driver.implicitly_wait(3)

   def close(self):
       self.driver.delete_all_cookies()
       self.driver.quit()
