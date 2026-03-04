import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcLayout(BoxLayout):
    def append_text(self, text):
        self.display.text += text

    def calculate(self, expression):
        try:
            # eval() evaluates the string as a math problem
            self.display.text = str(eval(expression))
        except Exception:
            self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if __name__ == "__main__":
    CalculatorApp().run()