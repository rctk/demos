from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText
from rctk.zk.widgets import Combo

class Demo(object):
    title = "Combo"
    description = "Demonstrates the Combo control"

    def build(self, tk, parent):
        options = ((1, "Hello1"), (2, "World"), (3, "Bye"), (4, "Last one"))
        combo = Combo(tk, options[:-1])
        msg = StaticText(tk, "Make a selection")
        parent.append(combo)
        parent.append(msg)
        combo.add(*options[-1])

        def click(e):
            msg.text = "You clicked " + dict(options)[combo.value]

        combo.click = click
        combo.paging = 3
        combo.header = "desc"        

        ## select the item with key 2 - "World"
        combo.value = 2


Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

