from framework.base_elements.base_element import BaseElement
from selenium.webdriver.common.by import By


class Text(BaseElement):

    def get_text(self):
        return self.screen.context.driver.find_element(By.XPATH, self.locator).text
