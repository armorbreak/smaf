from framework.base_elements import BaseScreen


class ScreenManager:
    def __init__(self, context):
        self.context = context
        self.screens = {
            "BaseScreen": BaseScreen,
        }

    def get_screen(self, screen_name):
        return self.screens[screen_name](self.context) if screen_name in self.screens.keys() else None
