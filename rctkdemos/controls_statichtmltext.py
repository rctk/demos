from demos import serve_demo
from rctk.widgets import StaticHTMLText

class Demo(object):
    title = "StaticHTMLText"
    description = "Demonstrates the StaticHTMLText control"

    def build(self, tk, parent):
        static = StaticHTMLText(tk, "StaticText just <i>display</i> <b>some text</b>")
        parent.append(static)

if __name__ == '__main__':
    serve_demo(Demo)

