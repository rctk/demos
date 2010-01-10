from demos import serve_demo
from rctk.widgets import StaticText

class Demo(object):
    title = "StaticText"
    description = "Demonstrates the StaticText control"

    def build(self, tk, parent):
        static = StaticText(tk, "StaticText just display <b>some text</b>")
        parent.append(static)

if __name__ == '__main__':
    serve_demo(Demo)

