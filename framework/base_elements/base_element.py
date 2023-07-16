from framework.base_elements.base_screen import BaseScreen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BaseElement:

    def __init__(self, name: str, locator: str, screen: BaseScreen):
        self.name = name
        self.locator = locator
        self.screen = screen

    def click(self, by=By.XPATH):
        self.screen.context.driver.find_element(value=self.locator, by=by).click()

    def wait_for_appear(self, by=By.XPATH, timeout=15):
        WebDriverWait(self.screen.context.driver, timeout).until(ec.visibility_of_element_located((by, self.locator)))

    def wait_for_disappear(self, by=By.XPATH, timeout=15):
        WebDriverWait(self.screen.context.driver, timeout).until(ec.invisibility_of_element_located((by, self.locator)))

    def is_visible(self, timeout=15):
        try:
            self.wait_for_appear(timeout=timeout)
            return True
        except TimeoutException:
            return False

