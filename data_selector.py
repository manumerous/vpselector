__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"


import pandas as pd
from pandas.core.indexes.base import Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

try:
    from src.main_window import MainWindow
except:
    from visual_dataframe_selector.src.main_window import MainWindow


def select_visual_data(data_df, plot_config_dict):
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data_df, plot_config_dict)
    app.exec_()
    return w.cropped_data_df


def select_visual_data_in_running_app(data_df, plot_config_dict, app):
    w = MainWindow(data_df, plot_config_dict)
    app.processEvents()  # Process events once before waiting
    while w.isVisible():  # Loop until window is closed
        app.processEvents()
    return w.cropped_data_df
