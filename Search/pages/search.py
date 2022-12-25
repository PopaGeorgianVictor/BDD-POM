from Dropdown.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class Search(BasePage):

    SEARCH_BAR = (By.ID, "myInput")
    ELEM = (By.LINK_TEXT, "LISTS")

    def navigate_to_page(self):
        self.driver.get()

    def search_for_elem(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('lists')
        elem = self.driver.find_element(*self.ELEM)
        actual_search = elem.text
        expected_search = "LISTS"
        assert actual_search == expected_search, f'Error: expected: {expected_search}, actual: {actual_search}'

    def click_on_elem(self):
        self.driver.find_element(*self.ELEM).click()
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(By.CSS_SELECTOR, "a[title='Python Tutorial']")
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")