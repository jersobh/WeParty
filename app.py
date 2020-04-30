import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from module.buttons import ImageButton, LabelButton, ImageButtonSelectable
from kivy.core.window import Window
from requests import get


from kivy.utils import platform
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from module import devices


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

    def build(self):
        self.icon = 'assets/icon.png'
        self.title = 'WeParty'
        Window.clearcolor = (0.5, 0.5, 0.5, 1)
        Window.size = (400, 700)
        return Builder.load_file("main.kv")

    def get_my_ip(self):
        ip = get('https://api.ipify.org').text
        return ip

    def add_network(self, network_name):
        create = devices.VirtualDevice.create(network_name)
        popup = Popup(title='Create network', content=Label(text=create),
              auto_dismiss=True, size_hint=(None, None), size=(340, 100))
        popup.open()

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
