import os

from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Image
from rctk.resourceregistry import addResource, FileResource

class Demo(object):
    title = "Image"
    description = "Demonstrates the Image control"

    def __init__(self):
        self.counter = 0
        self.resources = []

    def h(self, e):
        self.counter += 1
        self.img.resource = self.resources[self.counter % 12]
        self.tk.set_timer(self.h, 250)

    def build(self, tk, parent):
        self.tk = tk
        for i in range(0, 12):
            r = addResource(FileResource("resources/nyancat-%d.png" % i,
                                         name="nyancat-%d" % i,
                                         type="image/png"))
            self.resources.append(r)
        self.img = Image(tk, resource=self.resources[0])
        parent.append(self.img)
        self.tk.set_timer(self.h, 250)
    
    
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

