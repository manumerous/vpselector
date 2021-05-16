__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"


import pandas as pd
from pandas.core.indexes.base import Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from src.main_window import MainWindow


def select_visual_data(data_df, plot_config_dict):
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data_df, plot_config_dict)
    app.exec_()
    return w.cropped_data_df
