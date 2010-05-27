import os

from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import ImageFile

class Demo(object):
    title = "Image"
    description = "Demonstrates the Image control"

    def build(self, tk, parent):
        img = ImageFile(tk, os.path.join(os.path.dirname(__file__), 'resources/googlecodelogo.png'), title='Google Code')
        parent.append(img)
    
    
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

