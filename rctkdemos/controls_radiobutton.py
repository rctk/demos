from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import CheckBox, CheckBoxGroup, StaticText
from rctk.layouts import HBox

class Demo(object):
    title = "CheckBox"
    description = "Demonstrates the CheckBox control"

    def build(self, tk, parent):
        parent.setLayout(HBox())
        box1 = CheckBox(tk)
        group1 = CheckBoxGroup(tk)
        box2 = CheckBox(tk, checked=True, value="Option 1", group=group1)
        box3 = CheckBox(tk, group=group1, value="Option 2")
        box4 = CheckBox(tk, group=group1, value="Option 3")
        parent.append(box1)
        parent.append(box2)
        parent.append(box3)
        parent.append(box4)
        box1.checked = True

        selection = StaticText(tk, text=group1.value)
        parent.append(selection)
        def handle_group(e):
            selection.text = group1.value
        group1.click = handle_group


if __name__ == '__main__':
    serve_demo(Demo)

Standalone = standalone(Demo)
