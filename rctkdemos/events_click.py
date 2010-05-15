from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText, Button
from rctk.layouts import Grid

class Demo(object):
    title = "ClickHandler"
    description = "Demonstrates a click handler on a button"

    def __init__(self):
        self.counter = 0

    def click_handler(self, event):
        self.counter += 1
        if self.counter == 1:
            self.message.text = "%d click" % self.counter
        else:
            self.message.text = "%d clicks" % self.counter

    def build(self, tk, parent):
        parent.setLayout(Grid(columns=2))

        button = Button(tk, "Click me")
        self.message = StaticText(tk, "0 clicks")

        button.click = self.click_handler

        parent.append(self.message)
        parent.append(button)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

