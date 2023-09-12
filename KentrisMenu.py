from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class KentrisMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(KentrisMenu, self).__init__(**kwargs)
        self.kentris = Image(source='kentris.png')
        self.add_widget(self.kentris)


