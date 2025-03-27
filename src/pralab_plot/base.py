from bokeh.plotting import figure

class BaseFigure(figure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
