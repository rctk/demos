from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import CheckBox, StaticText
from rctk.layouts import VBox

class Demo(object):
    title = "CheckBox"
    description = "Demonstrates the CheckBox control"

    def build(self, tk, parent):
        parent.setLayout(VBox())
        box1 = CheckBox(tk, text="Option 1")
        box2 = CheckBox(tk, checked=True, text="Option 2")
        box3 = CheckBox(tk, text="Option 3")
        box4 = CheckBox(tk, text="Option 4")
        parent.append(box1)
        parent.append(box2)
        parent.append(box3)
        parent.append(box4)
        box4.checked = True

        selection = StaticText(tk)
        parent.append(selection)

        def handle_click(e):
            selection.text = ", ".join(b.text for b in (box1, box2, box3, box4) if b.checked)

        box1.click = box2.click = box3.click = box4.click = handle_click
        handle_click(None)

if __name__ == '__main__':
    serve_demo(Demo)

Standalone = standalone(Demo)
