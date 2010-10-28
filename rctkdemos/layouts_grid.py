from rctkdemos.demos import serve_demo
from rctk.widgets import StaticText
from rctk.layouts import GridLayout

class Demo(object):
    title = "Grid"
    description = "Demonstrates the Grid using padding and different col/rowspans"

    def build(self, tk, parent):
        parent.setLayout(GridLayout(columns=3, padx=2, pady=3))
        parent.append(StaticText(tk, "Win 1", background="red"), colspan=2)
        parent.append(StaticText(tk, "Win 2", background="yellow"))
        parent.append(StaticText(tk, "Win 3", background="green"), rowspan=2)
        parent.append(StaticText(tk, "Win 4", background="orange"))
        parent.append(StaticText(tk, "Win 5", background="blue"))
        parent.append(StaticText(tk, "Win 6", background="pink"))
        parent.append(StaticText(tk, "Win 7", background="grey"))
        parent.append(StaticText(tk, "Win 8", background="brown"), rowspan=2, colspan=2)        
        parent.layout()

if __name__ == '__main__':
    serve_demo(Demo)

