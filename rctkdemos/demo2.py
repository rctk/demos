from rctk.widgets import StaticText
from rctk.layouts import TabbedLayout

from rctk.app import JWin

##
## Test the tabbed layout
class Demo(object):
    def __init__(self):
        pass

    def run(self, tk):
        root = tk.root()
        root.setLayout(TabbedLayout())
        root.append(StaticText(tk, "This is tab 1" * 10), title="tab 1");
        root.append(StaticText(tk, "This is tab 2" * 10), title="tab 2");
        root.append(StaticText(tk, "This is tab 3" * 10), title="tab 3");
        root.append(StaticText(tk, "This is tab 4" * 10), title="tab 4");


if __name__ == '__main__':
    j = JWin(Demo)
    j.start()
