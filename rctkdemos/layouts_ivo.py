from rctkdemos.demos import serve_demo
from rctk.widgets import StaticText
from rctk.layouts import Grid

class Demo(object):
    title = "Grid"
    description = "Demonstrates the Grid using a 2x2 layout"

    def build(self, tk, parent):
        parent.setLayout(Grid(columns=2))
        parent.append(StaticText(tk, "(1,1)"))
        parent.append(StaticText(tk, "(1,2)"))
        parent.append(StaticText(tk, "(2,1)"))
        parent.append(StaticText(tk, "(2,2)"))
        parent.layout()

if __name__ == '__main__':
    serve_demo(Demo)

