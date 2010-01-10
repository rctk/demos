from demos import serve_demo
from rctk.widgets import StaticText
from rctk.layouts import BorderLayout

class Demo(object):
    title = "BorderLayout"
    description = "Demonstrates the BorderLayout"

    def build(self, tk, parent):
        parent.setLayout(BorderLayout())
        parent.append(StaticText(tk, "north"), direction="north")
        parent.append(StaticText(tk, "east"), direction="east")
        parent.append(StaticText(tk, "south"), direction="south")
        parent.append(StaticText(tk, "west"), direction="west")
        parent.append(StaticText(tk, "center"), direction="center")

if __name__ == '__main__':
    serve_demo(Demo)

