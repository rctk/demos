from demos import serve_demo
from rctk.widgets import List

class Demo(object):
    title = "List"
    description = "Demonstrates the List control"

    def build(self, tk, parent):
        l = List(tk, ((1, "Hello"), (2, "World"), (3, "Bye")))
        parent.append(l)
        l.add(4, "almost last one")
        l.add(5, "Last one")

if __name__ == '__main__':
    serve_demo(Demo)

