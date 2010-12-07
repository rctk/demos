from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, StaticText, CheckBox

class Demo(object):
    title = "State"
    description = "Demonstrates control state"

    def build(self, tk, parent):
        button = Button(tk, "Click me!")
        t1 = StaticText(tk, 'Enabled:')
        c1 = CheckBox(tk)
        t2 = StaticText(tk, 'Visible:')
        c2 = CheckBox(tk, checked=True)

        def toggle_state(x):
            button.enabled = not button.enabled
        c1.click = toggle_state
        def toggle_visibility(x):
            button.visible = c2.checked
        c2.click = toggle_visibility

        button.enabled = False
        parent.append(button)
        parent.append(t1)
        parent.append(c1)
        parent.append(t2)
        parent.append(c2)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

