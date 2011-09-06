from rctk.widgets import StaticHTMLText
from rctk.layouts import GridLayout
from rctk.app import App

from rctkdemos.all import DemoPanel, make_py

from rctkdemos.compat import highlight

import sys

class DemoRunner(App):
    def __init__(self, demo_class):
        self.demo = demo_class()

    def load_source(self, klass):
        mod = sys.modules[klass.__module__]
        sourcecode = open(make_py(mod.__file__), "r").read()
        return highlight(sourcecode)

    def run(self, tk):
        p = DemoPanel(tk)
        tk.root().append(p, sticky=GridLayout.NEWS)
        self.demo.build(tk, p.buildpanel)
        p.sourcepanel.append(StaticHTMLText(tk, self.load_source(self.demo)))
        p.descriptionpanel.append(StaticHTMLText(tk, self.demo.description))
        tk.root().layout()


def serve_demo(demo_class):
    from rctk.webpy import serve
    serve(DemoRunner, demo_class)

def standalone(demo_class):
    def factory():
        return DemoRunner(demo_class)
    return factory
