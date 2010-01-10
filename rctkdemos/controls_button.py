from demos import serve_demo
from rctk.widgets import Button

class Demo(object):
    title = "Button"
    description = "Demonstrates the Button control"

    def build(self, tk, parent):
        button = Button(tk, "Click me!")
        parent.append(button)

if __name__ == '__main__':
    serve_demo(Demo)

