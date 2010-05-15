from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Image

class Demo(object):
    title = "Image"
    description = "Demonstrates the Image control"

    def build(self, tk, parent):
        img = Image(tk, 'http://www.gstatic.com/codesite/ph/images/defaultlogo.png', title='Google Code')
        parent.append(img)
    
    
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

