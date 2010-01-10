from demos import serve_demo
from rctk.widgets import StaticText
from rctk.layouts import GridLayout

class Demo(object):
    title = "GridLayout"
    description = "Demonstrates the GridLayout using a 2x2 layout"

    def build(self, tk, parent):
        parent.setLayout(GridLayout(rows=2, columns=2))
        parent.append(StaticText(tk, "(1,1)"))
        parent.append(StaticText(tk, "(1,2)"))
        parent.append(StaticText(tk, "(2,1)"))
        parent.append(StaticText(tk, "(2,2)"))

if __name__ == '__main__':
    serve_demo(Demo)

