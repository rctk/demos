from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import RadioButton, RadioGroup, StaticText
from rctk.layouts import VBox

class Demo(object):
    title = "CheckBox"
    description = "Demonstrates the CheckBox control"

    def build(self, tk, parent):
        parent.setLayout(VBox())
        b1 = RadioButton(tk, text="Option 1", value=1)
        b2 = RadioButton(tk, text="Option 2", value=2)
        b3 = RadioButton(tk, text="Option 3", value=3)
        b4 = RadioButton(tk, text="Option 4", value=4)
        parent.append(b1)
        parent.append(b2)
        parent.append(b3)
        parent.append(b4)

        def handle_group(e):
            selection.text = "Selected: %d" % group.value
        group = RadioGroup(b1, b2, b3, b4)
        group.selected = b3
        group.click = handle_group

        selection = StaticText(tk, text="Selected: %d" % group.value)
        parent.append(selection)



if __name__ == '__main__':
    serve_demo(Demo)

Standalone = standalone(Demo)
