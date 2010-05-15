from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import StaticText, Button
from rctk.layouts import Grid

class Demo(object):
    title = "TimerHandler"
    description = "Demonstrates timers in RCTK"

    def __init__(self):
        self.counter = 0
        self.running = False

    def startstop_handler(self, event):
        if self.running:
            self.startstop.text = "Start"
            self.running = False
            ## cancel the running timer
        else:
            self.startstop.text = "Stop"
            self.running = True
            self.tk.set_timer(self.timer_handler, 1000)

    def timer_handler(self, event):
        if not self.running:
            return # stop was pressed

        self.counter += 1
        if self.counter == 1:
            self.message.text = "%d events" % self.counter
        else:
            self.message.text = "%d events" % self.counter
        self.tk.set_timer(self.timer_handler, 1000)

    def build(self, tk, parent):
        self.tk = tk
        parent.setLayout(Grid(columns=2))

        self.startstop = Button(tk, "Start")
        self.message = StaticText(tk, "0 events")
        self.startstop.click = self.startstop_handler

        parent.append(self.message)
        parent.append(self.startstop)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

