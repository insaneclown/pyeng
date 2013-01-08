from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from gui.screens import *

class PyEngApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu'))
        return screen_manager

PyEngApp().run()
