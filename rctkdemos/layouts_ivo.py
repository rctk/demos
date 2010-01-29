from rctkdemos.demos import serve_demo
from rctk.widgets import StaticText
from rctk.layouts import IvoLayout

class Demo(object):
    title = "IvoLayout"
    description = "Demonstrates the IvoLayout using a 2x2 layout"

    def build(self, tk, parent):
        parent.setLayout(IvoLayout(columns=2))
        parent.append(StaticText(tk, "(1,1)"))
        parent.append(StaticText(tk, "(1,2)"))
        parent.append(StaticText(tk, "(2,1)"))
        parent.append(StaticText(tk, "(2,2)"))
        parent.layout()

if __name__ == '__main__':
    serve_demo(Demo)

