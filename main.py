from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.core.window import Window
import akivymd

Window.size = (1920, 1016)
Window.minimum_width, Window.minimum_height = Window.size


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.size_y = NumericProperty(0)
        self.size_x = NumericProperty(0)

    def build(self):
        self.size_x, self.size_y = Window.size
        self.theme_cls.theme_style = "Light"
        self.size_x, self.size_y = Window.size
        self.title = "POCKET"


MainApp().run()
