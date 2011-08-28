from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, Window, StaticText

class Demo(object):
    title = "Window"
    description = "Demonstrates the Window control"

    def open_modal(self, e):
        if self.modal_window:
            self.modal_window.shut()
            self.modal_window = None
        else:
            self.modal_window = Window(self.tk, "Modal window", modal=True)
            self.modal_window.append(StaticText(self.tk, "I'm a modal window"))
            self.modal_window.open()

            def handle_close(e):
                self.modal_window = None

            self.modal_window.close = handle_close

    def open_nonmodal(self, e):
        if self.nonmodal_window:
            self.nonmodal_window.shut()
            self.nonmodal_window = None
        else:
            self.nonmodal_window = Window(self.tk, "Modal window", modal=False)
            self.nonmodal_window.append(StaticText(self.tk, "I'm a non-modal window"))
            self.nonmodal_window.open()

            def handle_close(e):
                self.nonmodal_window = None

            self.nonmodal_window.close = handle_close

    def open_a_lot(self, e):
        def hide_all():
            if self.lots:
                for w in self.lots:
                    w.shut()
                    w.destroy()
                self.lots = []

        if self.lots:
            hide_all()
            return

        for p in (("left", "top"), ("center", "top"), ("right", "top"), 
                  ("left", "center"), ("center", ), ("right", "center"),
                  ("left", "bottom"), ("center", "bottom"), ("right", "bottom")):
            l = ", ".join(p)
            w = Window(self.tk, l + " window", position=p)
            w.append(StaticText(self.tk, ", ".join(p)))
            w.open()
            w.close = lambda e: hide_all()
            self.lots.append(w)

    def build(self, tk, parent):
        self.tk = tk
        self.lots = []

        modal = Button(tk, "Click to open a modal window")
        nonmodal = Button(tk, "Click to open a non-modal window")
        alot = Button(tk, "Click to open a lot of windows")

        self.modal_window = None
        self.nonmodal_window = None
        
        modal.click = self.open_modal
        nonmodal.click = self.open_nonmodal
        alot.click = self.open_a_lot

        parent.append(modal)
        parent.append(nonmodal)
        parent.append(alot)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

