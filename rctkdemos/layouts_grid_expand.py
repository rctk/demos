from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText, Panel
from rctk.layouts import StaticVBox

class Demo(object):
    title = "Control gravity"
    description = "Demonstrates expanding controls"

    def build(self, tk, parent):
        parent.setLayout(StaticVBox())
        parent.append(StaticText(tk, "No expanding\n(centered)", background="yellow"))
        parent.append(StaticText(tk, "Horizontal", background="orange"), sticky=StaticVBox.EAST|StaticVBox.WEST)
        parent.append(StaticText(tk, "V\ne\nr\nt\ni\nc\na\nl", background="yellow"), sticky=StaticVBox.NORTH|StaticVBox.SOUTH)
        parent.append(StaticText(tk, "Horizontal\nV\ne\nr\nt\ni\nc\na\nl", background="orange"), sticky=StaticVBox.NEWS)

        parent.layout()

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

