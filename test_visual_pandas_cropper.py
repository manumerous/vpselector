__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"

import pandas as pd
from PyQt5 import QtWidgets
import sys

from src.main_window import MainWindow


def test_visual_pandas_cropper():
    plot_config_dict = {
        "x_axis_col": "timestamp",
        "sub_plt1_data": ["q0", "q1", "q2", "q3"],
        "sub_plt2_data": ["u0", "u1", "u2", "u3", "u4", "u5", "u6", "u7"]}
    data_df = pd.read_csv("resources/output.csv", index_col=0)

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow(data_df, plot_config_dict)
    app.exec_()
    print(w.cropped_data_df)
    return


if __name__ == "__main__":
    test_visual_pandas_cropper()
