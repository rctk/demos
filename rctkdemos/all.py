from rctk.widgets import StaticHTMLText, Panel
from rctk.layouts import TabbedLayout
from rctk.app import App

from rctkdemos.compat import highlight

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

class Demo(App):
    title = "RCTK Demo"

    def __init__(self):
        pass

    def load_demo(self, name):
        mod = __import__(name, globals(), locals(), []) #, -1)
        demo = mod.Demo()
        return demo

    def load_source(self, name):
        mod = __import__(name, globals(), locals(), []) #, -1)
        sourcecode = open(make_py(mod.__file__), "r").read()
        return highlight(sourcecode)

    def load_demos(self, demos, panel, tk):
        for demoname in demos:
            demo = self.load_demo(demoname)
            sourcecode = self.load_source(demoname)

            demopanel = DemoPanel(tk)

            demopanel.descriptionpanel.append(StaticHTMLText(tk, demo.description))
            demopanel.sourcepanel.append(StaticHTMLText(tk, sourcecode))
            demo.build(tk, demopanel.buildpanel)

            panel.append(demopanel, title=demo.title)

    def build_simple_controls(self, panel, tk):
        demos = ("controls_button", 'controls_statictext', 'controls_statichtmltext', 'controls_text', 'controls_checkbox', 'controls_dropdown', 'controls_list', 'controls_date', 'controls_state', 'controls_image')
        
        self.load_demos(demos, panel, tk)

    def build_advanced_controls(self, panel, tk):
        demos = ('controls_date', ) # XXX'controls_grid')
        self.load_demos(demos, panel, tk)

    def build_layouts(self, panel, tk):
        demos = ("layouts_grid", "layouts_grid_gravity", "layouts_grid_expand" )
        self.load_demos(demos, panel, tk)

    def build_events(self, panel, tk):
        demos = ("events_click", 'events_checkbox', 'events_timer')
        self.load_demos(demos, panel, tk)

    def build_xml(self, panel, tk):
        demos = ("xml_simple", ) # XXX "xml_complex")
        self.load_demos(demos, panel, tk)

    def build_apps(self, panel, tk):
        demos = ("app_calculator", )
        self.load_demos(demos, panel, tk)

    def run(self, tk):
        root = tk.root()

        root.setLayout(TabbedLayout())

        self.controls_panel = Panel(tk)
        self.controls_panel.setLayout(TabbedLayout())
        self.advanced_panel = Panel(tk)
        self.advanced_panel.setLayout(TabbedLayout())
        self.layouts_panel = Panel(tk)
        self.layouts_panel.setLayout(TabbedLayout())
        self.events_panel = Panel(tk)
        self.events_panel.setLayout(TabbedLayout())
        self.xml_panel = Panel(tk)
        self.xml_panel.setLayout(TabbedLayout())
        self.apps_panel = Panel(tk)
        self.apps_panel.setLayout(TabbedLayout())

        self.mysource = Panel(tk)

        root.append(self.controls_panel, title="Simple Controls")
        root.append(self.advanced_panel, title="Advanced Controls")
        root.append(self.layouts_panel, title="Layouts")
        root.append(self.events_panel, title="Events")
        root.append(self.xml_panel, title="XML")
        root.append(self.apps_panel, title="Apps")
        root.append(self.mysource, title="My Source")

        self.build_simple_controls(self.controls_panel, tk)
        self.build_advanced_controls(self.advanced_panel, tk)
        self.build_layouts(self.layouts_panel, tk)
        self.build_events(self.events_panel, tk)
        self.build_xml(self.xml_panel, tk)
        self.build_apps(self.apps_panel, tk)

        mysource = open(make_py(__file__), "r").read()
        self.mysource.append(StaticHTMLText(tk,highlight(mysource)))
        root.layout()

def main():
    """ for standalone running """
    from rctk.webpy import serve
    from rctk.sessions import Session, Manager
    import os

    manager = Manager(Session, Demo, os.getcwd())
    serve(manager)

