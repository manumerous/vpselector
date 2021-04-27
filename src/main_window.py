
__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"

from src import ConfirmSelectionWindow
from src import MplWidget

from PyQt5 import QtWidgets, QtCore

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import SpanSelector

import pandas as pd


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data_df, plot_config_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Visual Pandas Cropper")

        self.data_df = data_df
        self.cropped_data_df = pd.DataFrame()

        # Prepare vertical col name and drop it from the plot config dict
        self.x_axis_col = plot_config_dict["x_axis_col"]
        self.plot_config_dict = plot_config_dict
        self.plot_config_dict.pop("x_axis_col", None)

        self.x_axis_data = self.data_df[self.x_axis_col]
        self.x_start = self.x_axis_data.iloc[0]
        self.x_end = self.x_axis_data.iloc[-1]
        print(self.x_end)

        self.setup_plots()

        # Create toolbar for simultaneous manipulation of all subplots
        self.addToolBar(NavigationToolbar(self.plt.canvas, self))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plt)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def setup_plots(self):

        subplot_keys = list(self.plot_config_dict.keys())
        subplot_count = len(subplot_keys)

        self.plt = MplWidget(self, subplot_count=subplot_count)

        for i in range(subplot_count):

            subplot_key = subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            for topic in subplot_topics_list:
                self.plt.canvas.subplot_axes[i].plot(
                    self.data_df[self.x_axis_col], self.data_df[topic], label=topic)

                self.plt.canvas.subplot_axes[i].legend()

            self.plt.canvas.subplot_axes[i].span = SpanSelector(
                self.plt.canvas.subplot_axes[i],
                onselect=self.on_region_select_callback,
                direction="horizontal",
                minspan=1,
                useblit=True,
                span_stays=False,
                button=[1],
                rectprops={"facecolor": "green", "alpha": 0.3})

        self.plt.show

    def on_region_select_callback(self, min_x_val, max_x_val):
        self.plt.canvas.subplot_axes[0].set_xlim([min_x_val, max_x_val])
        print(min_x_val, max_x_val)
        dialog_window = ConfirmSelectionWindow()
        selection_accepted = dialog_window.exec_()

        self.plt.canvas.subplot_axes[0].set_xlim([self.x_start, self.x_end])

        if selection_accepted:
            print("selection accepted: ", min_x_val, max_x_val)
            cropped_df = self.crop_df(min_x_val, max_x_val)
            self.cropped_data_df = self.cropped_data_df.append(cropped_df)
            self.cropped_data_df = self.cropped_data_df.reset_index()
            print(self.cropped_data_df)

        return

    def crop_df(self, t_start, t_end):
        cropped_df = self.data_df[self.x_axis_data >= t_start]
        cropped_df = cropped_df[self.x_axis_data <= t_end]
        return cropped_df
