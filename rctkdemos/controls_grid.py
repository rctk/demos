from rctkdemos.demos import serve_demo, standalone
from rctk.widgets.grid import Grid, Column

class Demo(object):
    title = "Grid"
    description = "Demonstrates a simple Grid"

    def build(self, tk, parent):
        grid = Grid(tk, 
         [
            Column('Inv. No', width=55, sorttype=Column.INT),
            Column('Date', width=90, sorttype=Column.DATE),
            Column('Amount', width=80, sorttype=Column.FLOAT),
            Column('Tax', width=80, align=Column.RIGHT, sorttype=Column.FLOAT),
            Column('Total', width=80, align=Column.RIGHT, sorttype=Column.FLOAT),
            Column('Notes', width=150, sortable=False)
        ])
        parent.append(grid)
        for i in range(0, 20):
            grid.add((str(1000+i), "2010-01-%d" % (i+1), str(i), str(i*0.19), str(i*1.19), "Hello world, %d" % i))

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

