from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Text, StaticText
from rctk.layouts import VBox

class Demo(object):
    title = "Text"
    description = "Demonstrates the Text control"

    def build(self, tk, parent):
        parent.setLayout(VBox())
        text1 = Text(tk, value="Hello")
        text2 = Text(tk, rows=10, columns=40, value="World")

        s1 = StaticText(tk, "You typed: " + text1.value)
        s2 = StaticText(tk, "You typed: " + text2.value)

        def text1_changed(e):
            s1.text = "You typed: " + text1.value

        def text1_submitted(e):
            s1.text = "Submit!"

        def text2_changed(e):
            s2.text = "You typed: " + text2.value

        text1.keypress = text1_changed
        text1.submit = text1_submitted
        text2.keypress = text2_changed

        parent.append(text1)
        parent.append(s1)
        parent.append(text2)
        parent.append(s2)
    
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

