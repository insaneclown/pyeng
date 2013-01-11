from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from core.gui.screens import *
from core.gui.views import *

from core.db import sync_db


class PyEngApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu'))
        screen_manager.add_widget(TaskListScreen(name='task_list'))
        screen_manager.add_widget(UserListScreen(name='user_list'))
        screen_manager.add_widget(AddUserScreen(name='add_user'))
        return screen_manager

#PyEngApp().run()
sync_db()
