from rctkdemos.demos import serve_demo, standalone
from rctk.xmlbuilder import SimpleXMLBuilder

xmlui = """<?xml version="1.0"?>
<resource xmlns="http://www.wxwidgets.org/wxxrc" version="2.5.3.0">
    <object class="GridLayout">
        <columns>2</columns>
        <object class="Button" name="button">
            <text>Click me!</text>
        </object>
        <object class="StaticText" name="state">
            <text>|</text>
        </object>
    </object>
</resource>
"""
class Demo(object):
    title = "Simple XML"
    description = "Parsing a simple XML UI string"

    states = "/-\\|"

    def build(self, tk, parent):
        self.counter = 0
        s = SimpleXMLBuilder(parent, self)
        s.fromString(xmlui)
        self.button.click = self.doit

    def doit(self, event):
        self.state.text = self.states[self.counter%4]
        self.counter += 1
        
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

