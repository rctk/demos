from demos import serve_demo
from rctk.widgets import CheckBox, CheckBoxGroup

class Demo(object):
    title = "CheckBox"
    description = "Demonstrates the CheckBox control"

    def build(self, tk, parent):
        box1 = CheckBox(tk)
        group1 = CheckBoxGroup(tk)
        box2 = CheckBox(tk, checked=True, group=group1)
        box3 = CheckBox(tk, group=group1)
        box4 = CheckBox(tk, group=group1)
        parent.append(box1)
        parent.append(box2)
        parent.append(box3)
        parent.append(box4)

if __name__ == '__main__':
    serve_demo(Demo)

