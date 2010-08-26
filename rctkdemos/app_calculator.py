from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, StaticText
from rctk.layouts import GridLayout

class Calculator(object):
    title = "Calculator"
    description = "Sample calculator app"

    def build(self, tk, parent):
        parent.setLayout(GridLayout(rows=6, columns=4))

        self.value = 0

        self.display = StaticText(tk, str(self.value))

        self.clear = Button(tk, "C")
        self.dummy = StaticText(tk, " ")
        self.divide = Button(tk, "/")
        self.multiply = Button(tk, "x")

        self.b7  = Button(tk, "7")
        self.b8  = Button(tk, "8")
        self.b9  = Button(tk, "9")
        self.substract = Button(tk, "-")

        self.b4  = Button(tk, "4")
        self.b5  = Button(tk, "5")
        self.b6  = Button(tk, "6")
        self.plus = Button(tk, "+")

        self.b1  = Button(tk, "1")
        self.b2  = Button(tk, "2")
        self.b3  = Button(tk, "3")

        self.equals = Button(tk, "=")
        self.b0 = Button(tk, "0")
        self.point = Button(tk, ".")

        parent.append(self.display, row=0, col=0, colspan=4)

        parent.append(self.clear, row=1, col=0)
        parent.append(self.dummy, row=1, col=1)
        parent.append(self.divide, row=1, col=2)
        parent.append(self.multiply, row=1, col=3)

        parent.append(self.b7, row=2, col=0)
        parent.append(self.b8, row=2, col=1)
        parent.append(self.b9, row=2, col=2)
        parent.append(self.substract, row=2, col=3)

        parent.append(self.b4, row=3, col=0)
        parent.append(self.b5, row=3, col=1)
        parent.append(self.b6, row=3, col=2)
        parent.append(self.plus, row=3, col=3)

        parent.append(self.b1, row=4, col=0)
        parent.append(self.b2, row=4, col=1)
        parent.append(self.b3, row=4, col=2)
        parent.append(self.equals, row=4, col=3, rowspan=2, expand_vertical=True)

        parent.append(self.b0, row=5, col=0, colspan=2, expand_horizontal=True)
        parent.append(self.point, row=5, col=2)

        def add(num):
            self.value *= 10
            self.value += num
            self.display.text = str(self.value)

        def clear(e):
            self.value = 0
            self.display.text = str(self.value)

        self.clear.click = clear
        self.b0.click = lambda e: add(0)
        self.b1.click = lambda e: add(1)
        self.b2.click = lambda e: add(2)
        self.b3.click = lambda e: add(3)
        self.b4.click = lambda e: add(4)
        self.b5.click = lambda e: add(5)
        self.b6.click = lambda e: add(6)
        self.b7.click = lambda e: add(7)

Standalone = standalone(Calculator)

if __name__ == '__main__':
    serve_demo(Demo)

