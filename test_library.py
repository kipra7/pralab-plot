#!/usr/bin/env python3
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

def main():
    # Test import and instantiation of BaseFigure
    try:
        from pralab_plot.base import BaseFigure
        print("BaseFigure imported successfully")
    except Exception as e:
        print("Error importing BaseFigure:", e)
    
    # Test import and instantiation of IPyPlot
    try:
        from pralab_plot.plot.ipy_plot import IPyPlot
        print("IPyPlot imported successfully")
    except Exception as e:
        print("Error importing IPyPlot:", e)
        
    # Test import and instantiation of RealtimePlot
    try:
        # Assuming RealtimePlot class is defined in server.py in realtime_plot folder.
        from pralab_plot.plot.realtime_plot.server import RealtimePlot
        print("RealtimePlot imported successfully")
    except Exception as e:
        print("Error importing RealtimePlot:", e)
    
    # Attempt to create instances
    try:
        bf = BaseFigure()
        print("BaseFigure instance created")
    except Exception as e:
        print("Error creating BaseFigure instance:", e)
    
    try:
        import pandas as pd
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        ip = IPyPlot(df)
        print("IPyPlot instance created")
    except Exception as e:
        print("Error creating IPyPlot instance:", e)
    
    try:
        rt = RealtimePlot(x=[], y=[], plot_type="line")
        print("RealtimePlot instance created")
    except Exception as e:
        print("Error creating RealtimePlot instance:", e)

if __name__ == "__main__":
    main()
