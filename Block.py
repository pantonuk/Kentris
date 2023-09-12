from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class Block(Widget):
    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(0)

    def __init__(self, **kwargs):
       super().__init__(**kwargs)


    def change_color(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue