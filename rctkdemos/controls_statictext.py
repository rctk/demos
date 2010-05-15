from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText

class Demo(object):
    title = "StaticText"
    description = "Demonstrates the StaticText control"

    def build(self, tk, parent):
        static = StaticText(tk, "StaticText just display some text")
        parent.append(static)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

