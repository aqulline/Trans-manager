from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = (1920, 1016)
Window.minimum_width, Window.minimum_height = Window.size


class MainApp(MDApp):
    def build(self):
        print(Window.size)


MainApp().run()
