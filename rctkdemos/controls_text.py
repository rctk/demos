from demos import serve_demo, standalone
from rctk.widgets import Text
from rctk.layouts import VBox

class Demo(object):
    title = "Text"
    description = "Demonstrates the Text control"

    def build(self, tk, parent):
        parent.setLayout(VBox())
        text1 = Text(tk) # , "Text allows you to input text")
        text2 = Text(tk, rows=10, columns=40)
        parent.append(text1)
        parent.append(text2)
    
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

