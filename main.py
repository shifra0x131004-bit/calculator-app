from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

Window.clearcolor = (0.06, 0.12, 0.15, 1)


class GlassButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)
        with self.canvas.before:
            Color(0, 1, 0.95, 0.25)
            self.rect = RoundedRectangle(radius=[15])

        self.bind(pos=self.update, size=self.update)

    def update(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.padding = 15
        self.spacing = 10

        self.display = TextInput(
            readonly=True,
            halign="right",
            font_size=32,
            background_color=(0, 0, 0, 0),
            foreground_color=(0, 1, 0.95, 1)
        )
        self.add_widget(self.display)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        for b in buttons:
            btn = GlassButton(text=b, font_size=22)
            btn.bind(on_press=self.on_press)
            self.add_widget(btn)

    def on_press(self, instance):
        if instance.text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += instance.text


class CalculatorApp(App):
    def build(self):
        return Calculator()


CalculatorApp().run()
