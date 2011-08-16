from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Date, StaticText

class Demo(object):
    title = "Date"
    description = "Demonstrates the Date control. Click the input entry to make a calendar appear"

    def build(self, tk, parent):
        d = Date(tk) 
        s = StaticText(tk, "No date selected")

        def change(e):
            s.text = "Date selected: " + d.value

        d.change = change

        parent.append(d)
        parent.append(s)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

