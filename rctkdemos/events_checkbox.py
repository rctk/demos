from demos import serve_demo
from rctk.widgets import CheckBox

class Demo(object):
    title = "EventCheckBox"
    description = "Demonstrates events on the CheckBox control. \
        Click a checkbox to toggle its counter part."

    def click_handler(self, event):
        if event.control == self.checkbox1:
            self.checkbox2.toggle()
        else:
            self.checkbox1.toggle()
    
    def build(self, tk, parent):
        self.checkbox1 = CheckBox(tk)
        self.checkbox2 = CheckBox(tk, default=True)
        self.checkbox1.click = self.click_handler
        self.checkbox2.click = self.click_handler
        parent.append(self.checkbox1)
        parent.append(self.checkbox2)

if __name__ == '__main__':
    serve_demo(Demo)

