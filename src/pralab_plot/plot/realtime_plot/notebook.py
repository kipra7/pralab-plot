from bokeh.plotting import output_notebook, show
from bokeh.models import ColumnDataSource
from ...base import BaseFigure

class RealtimePlotNotebook:
    def __init__(self, plot_type='line', buffer_size=None, **kwargs):
        output_notebook()
        self.buffer_size = buffer_size
        self.figure = BaseFigure(**kwargs)
        self.source = ColumnDataSource(data=dict(x=[], y=[]))
        # Setup plot based on plot_type
        if plot_type in ('line', 'both'):
            self.figure.line('x', 'y', source=self.source)
        if plot_type in ('scatter', 'both'):
            self.figure.circle('x', 'y', source=self.source)
    
    def show(self):
        show(self.figure)
    
    def add_plot(self, x, y):
        new_data = dict(x=[x], y=[y])
        self.source.stream(new_data, rollover=self.buffer_size)
