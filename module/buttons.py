from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, BorderImage
import kivy.utils


class ImageButton(ButtonBehavior, Image):
    pass


class ImageButtonSelectable(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButtonSelectable, self).__init__(**kwargs)
        with self.canvas.before:
            BorderImage(
                size=(self.width + 100, self.height + 100),
                pos=(self.x - 50, self.y - 50),
                border=(10, 10, 10, 10),
            )
            self.canvas_border = BorderImage(rgb=(kivy.utils.get_color_from_hex("#ffffff")))
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#111111")))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[5,])
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(state=self.update_color)

    def update_color(self, *args):
        print("self.canvas_Color: ", self.canvas_color.rgb)
        print("STATE IS ", self.state)
        print("self.canvas_Color: ", self.canvas_color.rgb)
        if self.state == 'normal':
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#111111")))
        else:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#333333")))
        with self.canvas.before:
            Color(rgb=self.canvas_color.rgba)#self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#FFFFFF")))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[5,])

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size



class LabelButton(ButtonBehavior, Label):
    pass