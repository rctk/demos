from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Button, Window, StaticText

class Demo(object):
    title = "Window"
    description = "Demonstrates the Window control"

    def open_modal(self, e):
        if self.modal_window:
            self.modal_window._close()
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
            self.nonmodal_window._close()
            self.nonmodal_window = None
        else:
            self.nonmodal_window = Window(self.tk, "Modal window", modal=False)
            self.nonmodal_window.append(StaticText(self.tk, "I'm a non-modal window"))
            self.nonmodal_window.open()

            def handle_close(e):
                self.nonmodal_window = None

            self.nonmodal_window.close = handle_close

    def build(self, tk, parent):
        self.tk = tk
        modal = Button(tk, "Click to open a modal window")
        nonmodal = Button(tk, "Click to open a non-modal window")

        self.modal_window = None
        self.nonmodal_window = None
        
        modal.click = self.open_modal
        nonmodal.click = self.open_nonmodal

        parent.append(modal)
        parent.append(nonmodal)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

