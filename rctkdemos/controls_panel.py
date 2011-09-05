from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Panel, Button, StaticText
from rctk.layouts import HBox, VBox

class Demo(object):
    title = "Panel"
    description = "Demonstrates the Panel control"

    def build(self, tk, parent):
        parent.setLayout(HBox())
        p1 = Panel(tk,width=200, height=200)
        p2 = Panel(tk, scrolling=True, width=200, height=200)
        p2.setLayout(VBox())
        p1.append(StaticText(tk, "Non-scrolling panel"))
        p2.append(StaticText(tk, "Scrolling panel"))
        b = Button(tk, "Click me")
        p1.append(b)

        def click(e):
            p2.append(StaticText(tk, "Line added"))
            parent.layout()
            p2.scrollbottom()

        b.click = click

        parent.append(p1)
        parent.append(p2)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

