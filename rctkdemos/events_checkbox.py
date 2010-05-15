from rctkdemos.demos import serve_demo
from rctk.widgets import CheckBox, CheckBoxGroup, Text

class Demo(object):
    title = "EventCheckBox"
    description = "Demonstrates events on the CheckBox control. \
        Click a checkbox to toggle its counter part."

    def click_handler(self, event):
        if event.control == self.box1:
            self.box2.toggle()
        else:
            self.box1.toggle()
    
    def group_handler(self, event):
        self.text.value = event.control.value
    
    def build(self, tk, parent):
        self.box1 = CheckBox(tk, checked=True)
        self.box2 = CheckBox(tk)
        self.box1.click = self.click_handler
        self.box2.click = self.click_handler
        parent.append(self.box1)
        parent.append(self.box2)
        
        self.group = CheckBoxGroup(tk)
        self.group.click = self.group_handler
        self.box3 = CheckBox(tk, group=self.group, value="Hello", checked=True)
        self.box4 = CheckBox(tk, group=self.group, value="World")
        self.box5 = CheckBox(tk, group=self.group, value="Bye")
        self.text = Text(tk, value=self.group.value)
        parent.append(self.box3)
        parent.append(self.box4)
        parent.append(self.box5)
        parent.append(self.text)
    

if __name__ == '__main__':
    serve_demo(Demo)

