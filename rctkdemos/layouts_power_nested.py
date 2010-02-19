from rctkdemos.demos import serve_demo
from rctk.widgets import StaticText, Panel
from rctk.layouts import Grid, VBox

class Demo(object):
    title = "Nested Grid / VBox Layout"
    description = "Demonstrates nested layoutmanagers"

    def build(self, tk, parent):
        parent.setLayout(VBox())
        p1 = Panel(tk)
        p1.setLayout(Grid(columns=2))

        p1.append(StaticText(tk, " ( 1 , 1 ) "))
        p1.append(StaticText(tk, " ( 1 , 2 ) "))
        p1.append(StaticText(tk, " ( 2 , 1 ) "))
        p1.append(StaticText(tk, " ( 2 , 2 ) "))

        parent.append(p1)
        parent.append(StaticText(tk, "expanding 2 cols"), layout={"expand_horizontal":True})
        parent.layout()


if __name__ == '__main__':
    serve_demo(Demo)

