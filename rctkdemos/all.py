from rctk.widgets import StaticText, Panel
from rctk.layouts import TabbedLayout

from rctk.receiver import serve

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from os.path import splitext

def make_py(pyc):
    return splitext(pyc)[0] + ".py"

class DemoPanel(Panel):
    """
        Create a panel with three tabs: demo, source, description
    """

    def __init__(self, tk):
        super(DemoPanel, self).__init__(tk)
        self.setLayout(TabbedLayout())
        self.buildpanel = Panel(tk)
        self.sourcepanel = Panel(tk)
        self.descriptionpanel = Panel(tk)

        self.append(self.buildpanel, title="Demo")
        self.append(self.sourcepanel, title="Source")
        self.append(self.descriptionpanel, title="Description")

class Demo(object):
    def __init__(self):
        self.lexer = PythonLexer()
        self.formatter = HtmlFormatter(noclasses=True)

    def load_demo(self, name):
        mod = __import__(name, globals(), locals(), []) #, -1)
        demo = mod.Demo()
        return demo

    def load_source(self, name):
        mod = __import__(name, globals(), locals(), []) #, -1)
        sourcecode = open(make_py(mod.__file__), "r").read()
        return highlight(sourcecode, self.lexer, self.formatter)

    def load_demos(self, demos, panel, tk):
        for demoname in demos:
            demo = self.load_demo(demoname)
            sourcecode = self.load_source(demoname)

            demopanel = DemoPanel(tk)

            demopanel.descriptionpanel.append(StaticText(tk, demo.description))
            demopanel.sourcepanel.append(StaticText(tk, sourcecode))
            demo.build(tk, demopanel.buildpanel)

            panel.append(demopanel, title=demo.title)

    def build_simple_controls(self, panel, tk):
        demos = ("controls_button", 'controls_statictext', 'controls_text', 'controls_checkbox', 'controls_radiobutton', 'controls_dropdown', 'controls_list', 'controls_date')
        
        self.load_demos(demos, panel, tk)

    def build_layouts(self, panel, tk):
        demos = ("layouts_grid", "layouts_border", "layouts_ivo", "layouts_ivo_nested" )
        
        self.load_demos(demos, panel, tk)

    def build_events(self, panel, tk):
        demos = ("events_click", 'events_checkbox', 'events_radiobutton')
        
        self.load_demos(demos, panel, tk)


    def run(self, tk):
        root = tk.root()
        root.setLayout(TabbedLayout())

        self.controls_panel = Panel(tk)
        self.controls_panel.setLayout(TabbedLayout())
        self.layouts_panel = Panel(tk)
        self.layouts_panel.setLayout(TabbedLayout())
        self.events_panel = Panel(tk)
        self.events_panel.setLayout(TabbedLayout())

        self.mysource = Panel(tk)

        root.append(self.controls_panel, title="Simple Controls")
        root.append(self.layouts_panel, title="Layouts")
        root.append(self.events_panel, title="Events")
        root.append(self.mysource, title="My Source")

        self.build_simple_controls(self.controls_panel, tk)
        self.build_layouts(self.layouts_panel, tk)
        self.build_events(self.events_panel, tk)

        mysource = open(make_py(__file__), "r").read()
        self.mysource.append(StaticText(tk,highlight(mysource, self.lexer, self.formatter)))
        root.layout()

def main():
    serve(Demo)

if __name__ == '__main__':
    main()
