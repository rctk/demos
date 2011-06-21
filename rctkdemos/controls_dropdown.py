from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Dropdown

class Demo(object):
    title = "Dropdown"
    description = "Demonstrates the Dropdown control"

    def build(self, tk, parent):
        dropdown = Dropdown(tk, ((1, "Hello"), (2, "World"), (3, "Bye")))
        parent.append(dropdown)
        dropdown.add(4, "Last one")

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

