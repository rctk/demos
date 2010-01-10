from demos import serve_demo
from rctk.widgets import StaticText, Panel
from rctk.layouts import IvoLayout

class Demo(object):
    title = "Nested IvoLayout"
    description = "Demonstrates a nested IvoLayout"

    def build(self, tk, parent):
        parent.setLayout(IvoLayout(columns=1))
        p1 = Panel(tk)
        p1.setLayout(IvoLayout(columns=2))

        p1.append(StaticText(tk, " ( 1 , 1 ) "))
        p1.append(StaticText(tk, " ( 1 , 2 ) "))
        p1.append(StaticText(tk, " ( 2 , 1 ) "))
        p1.append(StaticText(tk, " ( 2 , 2 ) "))

        parent.append(p1)
        parent.append(StaticText(tk, "expanding 2 cols"), layout={"expand_horizontal":True})


if __name__ == '__main__':
    serve_demo(Demo)

