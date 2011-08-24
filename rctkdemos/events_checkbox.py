from rctkdemos.demos import serve_demo
from rctk.widgets import CheckBox

class Demo(object):
    title = "EventCheckBox"
    description = "Demonstrates events on the CheckBox control. \
        Click a checkbox to toggle its counter part."

    def click_handler(self, event):
        if event.control == self.box1:
            self.box2.toggle()
        else:
            self.box1.toggle()
    
    def build(self, tk, parent):
        self.box1 = CheckBox(tk, checked=True)
        self.box2 = CheckBox(tk)
        self.box1.click = self.click_handler
        self.box2.click = self.click_handler
        parent.append(self.box1)
        parent.append(self.box2)

if __name__ == '__main__':
    serve_demo(Demo)

