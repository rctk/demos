from rctk.widgets import Window, StaticText, Text, Button
from rctk.layouts import GridLayout

from rctk.app import JWin

class Demo(object):
    def __init__(self):
        self.i = 0

    def click(self):
        self.win2.append(StaticText(self.tk, "Click %d - %s!" % (self.i, self.text.value)))
        self.text.value = ""
        self.i += 1

    def run(self, tk):
        self.tk = tk
        self.win1 = Window(tk, "Button window")
        self.win1.setLayout(GridLayout(columns=3, rows=1));

        self.win2 = Window(tk, "Message window")
        tk.root().append(self.win1)
        tk.root().append(self.win2)

        self.text = Text(tk)

        button = Button(tk, "Hello")
        button.click = self.click

        self.win1.append(StaticText(tk, "Enter some data"))
        self.win1.append(self.text)
        self.win1.append(button)


if __name__ == '__main__':
    j = JWin(Demo)
    j.start()
