__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"


import pandas as pd
from pandas.core.indexes.base import Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from visual_pandas_curator.main_window import MainWindow

# use this function if no pyqt app is running
def select_visual_data(data_df, plot_config_dict):
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data_df, plot_config_dict)
    app.exec_()
    return w.cropped_data_df

# use this function to include the visual data selection in a running pyqt app
def select_visual_data_in_running_app(data_df, plot_config_dict, app):
    w = MainWindow(data_df, plot_config_dict)
    app.processEvents()  # Process events once before waiting
    while w.isVisible():  # Loop until window is closed
        app.processEvents()
    return w.cropped_data_df
