from demos import serve_demo, standalone
from rctk.widgets.grid import Grid, Column

class Demo(object):
    title = "Grid"
    description = "Demonstrates a simple Grid"

    def build(self, tk, parent):
        grid = Grid(tk, 
         [
            Column('Inv. No', width=55),
            Column('Date', width=90),
            Column('Amount', width=80),
            Column('Tax', width=80, align=Column.RIGHT),
            Column('Total', width=80, align=Column.RIGHT),
            Column('Notes', width=150, sortable=False)
        ])
        parent.append(grid)

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

