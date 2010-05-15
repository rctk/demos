from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, CheckBox

class Demo(object):
    title = "Disabled"
    description = "Demonstrates disabled controls"

    def build(self, tk, parent):
        button = Button(tk, "Click me!")
        c = CheckBox(tk)

        def toggle(x):
            button.state = not button.state
        c.click = toggle

        button.state = Button.DISABLED
        parent.append(button)
        parent.append(c)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

