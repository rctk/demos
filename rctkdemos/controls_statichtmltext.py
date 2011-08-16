from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticHTMLText

class Demo(object):
    title = "StaticHTMLText"
    description = "Demonstrates the StaticHTMLText control"

    def build(self, tk, parent):
        static = StaticHTMLText(tk, "StaticHTMLText <i>displays</i> <b>rich text</b>")
        parent.append(static)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

