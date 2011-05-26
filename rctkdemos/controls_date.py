from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Date

class Demo(object):
    title = "Date"
    description = "Demonstrates the Date control. Click the input entry to make a calendar appear"

    def build(self, tk, parent):
        d = Date(tk) 
        parent.append(d)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

