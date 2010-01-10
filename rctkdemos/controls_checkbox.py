from demos import serve_demo
from rctk.widgets import CheckBox

class Demo(object):
    title = "CheckBox"
    description = "Demonstrates the CheckBox control"

    def build(self, tk, parent):
        checkbox1 = CheckBox(tk, False)
        checkbox2 = CheckBox(tk, True)
        parent.append(checkbox1)
        parent.append(checkbox2)

if __name__ == '__main__':
    serve_demo(Demo)

