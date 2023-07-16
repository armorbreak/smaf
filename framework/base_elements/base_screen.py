import time
from framework.helpers.swipe_helper import get_swipe_coordinates


class BaseScreen:
    def __init__(self, context):
        self.context = context
        self.elements = {}
        self.required_elements = []

    def wait_for_screen_loaded(self, timeout=15):
        for element in self.required_elements:
            element.wait_for_appear(timeout=timeout)
        return self

    def swipe(self, direction, times=1, duration=500):
        coordinates = get_swipe_coordinates(direction, self.context.driver)
        for i in range(times):
            self.context.driver.swipe(coordinates['start_x'], coordinates['start_y'],
                                      coordinates['end_x'], coordinates['end_y'], duration)
            time.sleep(1)
