from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Dropdown, StaticText

class Demo(object):
    title = "Dropdown"
    description = "Demonstrates the Dropdown control"

    def build(self, tk, parent):
        options = ((1, "Hello"), (2, "World"), (3, "Bye"), (4, "Last one"))
        dropdown = Dropdown(tk, options[:-1])
        msg = StaticText(tk, "Make a selection")
        parent.append(dropdown)
        parent.append(msg)
        dropdown.add(*options[-1])

        def click(e):
            msg.text = "You clicked " + dict(options)[dropdown.value]

        dropdown.click = click

        ## select the item with key 2 - "World"
        dropdown.value = 2


Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

