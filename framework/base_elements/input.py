from framework.base_elements.base_element import BaseElement
from selenium.webdriver.common.by import By


class Input(BaseElement):
    def send_keys(self, text, by=By.XPATH):
        self.screen.context.driver.find_element(value=self.locator, by=by).send_keys(text)
