__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"


import pandas as pd
from pandas.core.indexes.base import Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from visual_pandas_curator.windows.main_window import MainWindow

# use this function if no pyqt app is running
def select_visual_data(data : pd.DataFrame , plot_config : dict):
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data, plot_config)
    app.exec_()
    return w.cropped_data

# use this function to include the visual data selection in a running pyqt app
def select_visual_data_in_running_app(data, plot_config : dict, app):
    w = MainWindow(data, plot_config)
    app.processEvents()  # Process events once before waiting
    while w.isVisible():  # Loop until window is closed
        app.processEvents()
    return w.cropped_data
