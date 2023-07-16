import time
from framework.helpers.swipe_helper import get_swipe_coordinates
from framework.base_elements import Button


class BaseScreen:

    def __init__(self, context):
        self.context = context
        self.elements = {
            "GooglePlayUpdateDeclineButton": Button("GooglePlayUpdateDeclineButton",
                                                    "//android.widget.Button[contains(@resource-id, 'resource_name_obfuscated') and contains(@text, 'НЕТ')]",
                                                    self)
        }
        self.required_elements = []

    def close_google_play_update_if_displayed(self):
        if self.context.driver.desired_capabilities['platformName'].lower() == "android":
            if self.elements["GooglePlayUpdateDeclineButton"].is_visible(timeout=2):
                self.elements["GooglePlayUpdateDeclineButton"].click()

    def wait_for_screen_loaded(self, timeout=15, check_google_play_popup=False):
        if check_google_play_popup:
            self.close_google_play_update_if_displayed()
        for element in self.required_elements:
            element.wait_for_appear(timeout=timeout)
        return self

    def swipe(self, direction, times=1, duration=500):
        coordinates = get_swipe_coordinates(direction, self.context.driver)
        for i in range(times):
            self.context.driver.swipe(coordinates['start_x'], coordinates['start_y'],
                                      coordinates['end_x'], coordinates['end_y'], duration)
            time.sleep(1)
