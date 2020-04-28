import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from module.buttons import ImageButton, LabelButton, ImageButtonSelectable
from kivy.core.window import Window
from requests import get


from kivy.utils import platform
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from module import devices

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (400, 700)
Window.set_title('WeParty')

class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class CreateNetworkScreen(Screen):
    pass


class MainApp(App):
    option_choice = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.set_title('WeParty')

    def build(self):
        return Builder.load_file("main.kv")

    def get_my_ip(self):
        ip = get('https://api.ipify.org').text
        return ip

    def add_network(self, network_name):
        create = devices.VirtualDevice.create(network_name)
        print(create)

    def change_screen(self, screen_id, screen_name, direction='forward', mode = ""):
        screen_manager = self.root.ids['screen_manager']
        if direction == 'forward':
            mode = "push"
            direction = 'left'
        elif direction == 'backwards':
            direction = 'right'
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_id
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)

        screen_manager.current = screen_id
        Window.set_title(screen_name)


MainApp().run()
