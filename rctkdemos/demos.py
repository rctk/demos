from rctk.widgets import Window, StaticText, Panel, StaticHTMLText

from all import DemoPanel, make_py

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

import sys

class DemoRunner(object):
    def __init__(self, demo_class):
        self.demo = demo_class()

    def load_source(self, klass):
        mod = sys.modules[klass.__module__]
        sourcecode = open(make_py(mod.__file__), "r").read()
        return highlight(sourcecode, PythonLexer(), HtmlFormatter(noclasses=True))

    def run(self, tk):
        p = DemoPanel(tk)
        tk.root().append(p)
        self.demo.build(tk, p.buildpanel)
        p.sourcepanel.append(StaticHTMLText(tk, self.load_source(self.demo)))
        p.descriptionpanel.append(StaticHTMLText(tk, self.demo.description))


def serve_demo(demo_class):
    serve(DemoRunner, demo_class)

def standalone(demo_class):
    def factory():
        return DemoRunner(demo_class)
    return factory
