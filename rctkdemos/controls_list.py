from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import List, StaticText
from rctk.layouts import GridLayout

class Demo(object):
    title = "List"
    description = "Demonstrates the List control"

    def build(self, tk, parent):
        parent.setLayout(GridLayout(rows=3, columns=2))
        parent.append(StaticText(tk, "Single"))
        parent.append(StaticText(tk, "Multiple"))
        l = List(tk, ((1, "Hello"), (2, "World"), (3, "Bye")))
        l2 = List(tk, ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"), (5, "Five")), multiple=True)
        parent.append(l)
        parent.append(l2)

        out1 = StaticText(tk, str(l.value))
        out2 = StaticText(tk, str(l2.value))

        def click1(event):
            out1.text = str(l.value)
        def click2(event):
            out2.text = str(l2.value)

        l.click = click1
        l2.click = click2
        parent.append(out1)
        parent.append(out2)

        ## Add some extra's
        l.add(4, "almost last one")
        l.add(5, "Last one")
        ## make selection
        l.value = [3]
        l2.value = [1, 3, 5]

        out1.text = str(l.value)
        out2.text = str(l2.value)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

