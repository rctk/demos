from rctkdemos.demos import serve_demo, standalone
from rctk.xmlbuilder import SimpleXMLBuilder

xmlui = """<?xml version="1.0"?>
<resource xmlns="http://www.wxwidgets.org/wxxrc" version="2.5.3.0">
    <object class="GridLayout">
        <columns>3</columns>
        <rows>5</rows>
        <object class="Button" name="button1">
            <text>Left</text>
            <flags>
              <row>0</row>
              <column>0</column>
            </flags>
        </object>
        <object class="Button" name="button2">
            <text>Right</text>
            <flags>
              <row>0</row>
              <column>2</column>
            </flags>
        </object>
        <object class="StaticText" name="state">
            <text>Hello World</text>
            <flags>
              <row>1</row>
              <column>0</column>
              <colspan>3</colspan>
            </flags>
        </object>
        <object class="Text">
            <value>Some default text</value>
            <flags>
              <row>2</row>
              <column>0</column>
              <colspan>2</colspan>
            </flags>
        </object>
        <object class="Dropdown">
            <items>
              <item>
                <key>1</key>
                <value>Option 1</value>
              </item>
              <item>
                <key>2</key>
                <value>Option 2</value>
              </item>
              <item>
                <key>3</key>
                <value>Option 3</value>
              </item>
              <item>
                <key>4</key>
                <value>Option 4</value>
              </item>
              <item>
                <key>5</key>
                <value>Option 5</value>
              </item>
            </items>
            <flags>
              <row>2</row>
              <column>2</column>
            </flags>
        </object>
        <object class="CheckBox" name="check">
            <checked>True</checked>
            <flags>
              <row>3</row>
              <column>0</column>
            </flags>
        </object>
        <object class="Grid">
            <cols>
              <col><name>Foo</name></col>
              <col><name>Bar</name></col>
             </cols>
             <flags>
               <row>3</row>
               <column>1</column>
               <colspan>2</colspan>
               <rowspan>2</rowspan>
             </flags>
        </object>
        <object class="Date">
            <flags>
              <row>4</row>
              <column>0</column>
            </flags>
        </object>
    </object>
</resource>
"""
class Demo(object):
    title = "Complex XML"
    description = "Complex nesting, layout, all kinds of controls"

    def build(self, tk, parent):
        self.counter = 0
        s = SimpleXMLBuilder(parent, self)
        s.fromString(xmlui)
        parent.layout()
        
Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

