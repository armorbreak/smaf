import time
from helpers.swipe_helper import get_swipe_coordinates
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BaseScreen:

    def __init__(self, context):
        self.context = context
        self.elements = {
            "GooglePlayUpdateDeclineButton": "//android.widget.Button[contains(@resource-id, 'resource_name_obfuscated') and contains(@text, 'НЕТ')]"
        }
        self.required_elements = []

    def wait_for_element_is_visible(self, element, by=By.XPATH, timeout=15):
        try:
            locator = self.elements[element]
        except KeyError:
            locator = element
        WebDriverWait(self.context.driver, timeout).until(ec.visibility_of_element_located((by, locator)))

    def wait_for_element_disappear(self, element, by=By.XPATH, timeout=15):
        try:
            locator = self.elements[element]
        except KeyError:
            locator = element
        WebDriverWait(self.context.driver, timeout).until(ec.invisibility_of_element_located((by, locator)))

    def close_google_play_update_if_displayed(self):
        if self.context.driver.desired_capabilities['platformName'].lower() == "android":
            if self.element_is_displayed("GooglePlayUpdateDeclineButton", timeout=2):
                self.click_element("GooglePlayUpdateDeclineButton")

    def wait_for_screen_loaded(self, timeout=15):
        self.close_google_play_update_if_displayed()
        for locator in self.required_elements:
            self.wait_for_element_is_visible(locator, timeout=timeout)
        return self

    def element_is_displayed(self, element, by=By.XPATH, timeout=0):
        try:
            locator = self.elements[element]
        except KeyError:
            locator = element
        try:
            self.wait_for_element_is_visible(locator, by=by, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def click_element(self, element, by=By.XPATH):
        try:
            locator = self.elements[element]
        except KeyError:
            locator = element
        self.context.driver.find_element(value=locator, by=by).click()

    def send_keys_to_element(self, element, text, by=By.XPATH):
        try:
            locator = self.elements[element]
        except KeyError:
            locator = element
        self.context.driver.find_element(value=locator, by=by).send_keys(text)

    def swipe(self, direction, times=1, duration=500):
        coordinates = get_swipe_coordinates(direction, self.context.driver)
        for i in range(times):
            self.context.driver.swipe(coordinates['start_x'], coordinates['start_y'],
                                      coordinates['end_x'], coordinates['end_y'], duration)
            time.sleep(1)
