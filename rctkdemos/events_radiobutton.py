from demos import serve_demo
from rctk.widgets.radiobutton import RadioButton, RadioButtonGroup

class Demo(object):
    title = "EventRadioButton"
    description = "Demonstrates events on the RadioButton control."

    def build(self, tk, parent):
        group = RadioButtonGroup(tk)
        radio1 = RadioButton(tk)
        radio2 = RadioButton(tk)
        radio3 = RadioButton(tk)
        
        print type(radio1.name)
        
        group.add(radio1)
        group.add(radio2)
        group.add(radio3)
        parent.append(radio1)
        parent.append(radio2)
        parent.append(radio3)
        
        radio1.value = "1"
        radio2.value = "2"
        radio3.value = "3"

if __name__ == '__main__':
    serve_demo(Demo)

