from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Text, Button, StaticText, Panel, Collection
from rctk.layouts import Grid


class Demo(object):
    title = "Collection"
    description = "Demonstrates the Collection control"
    
    def append(self, event):
        if len(self.text.value):
            self.collection.append(self.text.value)
            self.text.value = ''
    
    def remove(self, event):
        if len(self.text.value):
            self.collection.remove(self.text.value)
            self.text.value = ''
    
    def clear(self, event):
        self.collection.clear()
        self.text.value = ''
    
    def build(self, tk, parent):
        parent.setLayout(Grid(rows=2, columns=4, expand_vertical=True))
        self.text = Text(tk)
        append_button = Button(tk, 'Append')
        append_button.click = self.append
        remove_button = Button(tk, 'Remove')
        remove_button.click = self.remove
        clear_button = Button(tk, 'Clear')
        clear_button.click = self.clear
        parent.append(self.text)
        parent.append(append_button)
        parent.append(remove_button)
        parent.append(clear_button)
        self.collection = Collection(tk, StaticText)
        self.collection.extend(['Hello', 'World', 'Bye'])
        parent.append(self.collection)
    

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

