from demos import serve_demo, standalone
from rctk.widgets import Button

class Demo(object):
    title = "Button"
    description = "Demonstrates the Button control"

    def build(self, tk, parent):
        button = Button(tk, "Click me!")
        parent.append(button)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

