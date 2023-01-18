from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



class Browser:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)

   def close(self):
       self.driver.delete_all_cookies()
       self.driver.quit()
