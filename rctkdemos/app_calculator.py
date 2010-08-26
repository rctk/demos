from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, StaticText
from rctk.layouts import GridLayout

class Calculator(object):
    title = "Calculator"
    description = "Sample calculator application"

    def build(self, tk, parent):
        def reset():
            self.equation = ""
            self.digits = 0
            self.floating = 0
            self.in_float = False

        def val():
            if self.in_float:
                return "%d.%d" % (self.digits, self.floating)
            return str(self.digits)

        def digit(num):
            if self.in_float:
                self.floating *= 10
                self.floating += num
                self.display.text = val()
            else:
                self.digits *= 10
                self.digits += num
                self.display.text = str(self.digits)

        def clear(e):
            reset()
            self.display.text = str(self.digits)

        def point(e):
            if not self.in_float:
                self.in_float = True
                self.display.text = str(self.digits) + "."

        def op(operator):
            self.equation += "%d.%d%s" % (self.digits, self.floating, operator)
            self.digits = 0
            self.floating = 0
            self.in_float = False

        def equals(e):
            self.equation += val()
            try:
                res = eval(self.equation)
                if res == int(res):
                    self.display.text = "%d" % res
                else:
                    self.display.text = "%f" %  eval(self.equation)
            except ZeroDivisionError, e:
                self.display.text = "err"
            reset()

        reset()

        parent.setLayout(GridLayout(rows=6, columns=4))

        self.display = StaticText(tk, str(self.digits))

        ## buttons 0 .. 9
        for n in range(0, 10):
            b =  Button(tk, str(n))
            b.click = lambda e, n=n: digit(n)
            setattr(self, "b%d" % n, b)

        self.clear = Button(tk, "C")
        self.dummy = StaticText(tk, " ")
        self.divide = Button(tk, "/")
        self.multiply = Button(tk, "x")
        self.plus = Button(tk, "+")
        self.substract = Button(tk, "-")
        self.equals = Button(tk, "=")
        self.point = Button(tk, ".")

        self.clear.click = clear
        self.point.click = point
        self.plus.click = lambda e: op("+")
        self.substract.click = lambda e: op("-")
        self.multiply.click = lambda e: op("*")
        self.divide.click = lambda e: op("/")
        self.equals.click = equals

        parent.append(self.display, row=0, col=0, colspan=4)

        # C _ / *
        parent.append(self.clear, row=1, col=0)
        parent.append(self.dummy, row=1, col=1)
        parent.append(self.divide, row=1, col=2)
        parent.append(self.multiply, row=1, col=3)

        # 7 8 9 -
        parent.append(self.b7, row=2, col=0)
        parent.append(self.b8, row=2, col=1)
        parent.append(self.b9, row=2, col=2)
        parent.append(self.substract, row=2, col=3)

        # 4 5 6 +
        parent.append(self.b4, row=3, col=0)
        parent.append(self.b5, row=3, col=1)
        parent.append(self.b6, row=3, col=2)
        parent.append(self.plus, row=3, col=3)

        # 1 2 3 =
        parent.append(self.b1, row=4, col=0)
        parent.append(self.b2, row=4, col=1)
        parent.append(self.b3, row=4, col=2)
        parent.append(self.equals, row=4, col=3, rowspan=2, expand_vertical=True)

        # 0 .
        parent.append(self.b0, row=5, col=0, colspan=2, expand_horizontal=True)
        parent.append(self.point, row=5, col=2)

Demo = Calculator # demorunner expects this

Standalone = standalone(Calculator)

if __name__ == '__main__':
    serve_demo(Demo)
