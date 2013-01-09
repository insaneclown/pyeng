from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from gui.screens import *
from gui.views import *

class PyEngApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu'))
        screen_manager.add_widget(TaskListScreen(name='task_list'))
        screen_manager.add_widget(UserListScreen(name='user_list'))
        return screen_manager

PyEngApp().run()
