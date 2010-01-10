from demos import serve_demo
from rctk.widgets.radiobutton import RadioButton

class Demo(object):
    title = "RadioButton"
    description = "Demonstrates the RadioButton control"

    def build(self, tk, parent):
        parent.append(RadioButton(tk, False))

if __name__ == '__main__':
    serve_demo(Demo)

