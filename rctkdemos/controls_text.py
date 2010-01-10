from demos import serve_demo
from rctk.widgets import Text

class Demo(object):
    title = "Text"
    description = "Demonstrates the Text control"

    def build(self, tk, parent):
        text = Text(tk) # , "Text allows you to input text")
        parent.append(text)

if __name__ == '__main__':
    serve_demo(Demo)

