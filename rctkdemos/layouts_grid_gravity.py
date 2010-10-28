from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText, Panel
from rctk.layouts import GridLayout, VBox

class Demo(object):
    title = "Control gravity"
    description = "Demonstrates different gravity"

    def build(self, tk, parent):
        parent.setLayout(GridLayout(columns=3, static=True, rows=3, padx=1, pady=1))
        parent.append(StaticText(tk, "NW", background="yellow"), sticky=GridLayout.NORTH|GridLayout.WEST)
        parent.append(StaticText(tk, "N", background="orange"), sticky=GridLayout.NORTH)
        parent.append(StaticText(tk, "NE", background="yellow"), sticky=GridLayout.NORTH|GridLayout.EAST)
        parent.append(StaticText(tk, "W", background="orange"), sticky=GridLayout.WEST)
        parent.append(StaticText(tk, "X\nCENTER\nX", background="red"), sticky=GridLayout.CENTER)
        parent.append(StaticText(tk, "E", background="orange"), sticky=GridLayout.EAST)
        parent.append(StaticText(tk, "SW", background="yellow"), sticky=GridLayout.SOUTH|GridLayout.WEST)
        parent.append(StaticText(tk, "S", background="orange"), sticky=GridLayout.SOUTH)
        parent.append(StaticText(tk, "SE", background="yellow"), sticky=GridLayout.SOUTH|GridLayout.EAST)

        parent.layout()

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

