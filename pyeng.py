from kivy.app import App
from kivy.uix.label import Label

class PyEngApp(App):
    def build(self):
        return Label(text='Hello World')

PyEngApp().run()
