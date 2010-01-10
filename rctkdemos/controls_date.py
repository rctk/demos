from demos import serve_demo
from rctk.widgets import Date

class Demo(object):
    title = "Date"
    description = "Demonstrates the Date control"

    def build(self, tk, parent):
        d = Date(tk) 
        parent.append(d)

if __name__ == '__main__':
    serve_demo(Demo)

