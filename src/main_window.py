
__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"

try:
    from src.confirm_selection_window import ConfirmSelectionWindow
    from src.mpl_widget import MplWidget
except:
    from visual_dataframe_selector.src.confirm_selection_window import ConfirmSelectionWindow
    from visual_dataframe_selector.src.mpl_widget import MplWidget


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QPushButton

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import SpanSelector

import pandas as pd
import numpy as np
import seaborn as sns
import time
import copy

pd.set_option('mode.chained_assignment', None)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data_df, plot_config_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Visual Dataframe Selector")

        self.data_df = data_df
        self.cropped_data_df = pd.DataFrame()

        # Prepare vertical col name and drop it from the plot config dict
        self.x_axis_col = plot_config_dict["x_axis_col"]
        self.plot_config_dict = plot_config_dict
        self.plot_config_dict.pop("x_axis_col", None)

        self.x_axis_data = self.data_df[self.x_axis_col]
        self.x_start = self.x_axis_data.iloc[0]
        self.x_end = self.x_axis_data.iloc[-1]

        self.setup_plots()

        # Create toolbar for simultaneous manipulation of all subplots
        self.addToolBar(NavigationToolbar(self.data_plt.canvas, self))

        master_layout = QtWidgets.QGridLayout()

        text_label = QLabel(
            "Select Data by clicking the left mouse button and dragging the cursor")
        text_label.setFixedSize(600, 30)

        self.termination_button = QPushButton("Done selecting")
        self.termination_button.setFixedSize(150, 30)
        # connect signal
        self.termination_button.clicked.connect(self._terminate)

        self.save_csv_button = QPushButton("Save Result")
        self.save_csv_button.setFixedSize(150, 30)
        self.save_csv_button.setEnabled(False)
        # connect signal
        self.save_csv_button.clicked.connect(self._save_to_csv)

        # this label currently prevents resizing of the first column. Shall be adapted in the future
        # master_layout.addWidget(text_label, 0, 1)
        master_layout.setColumnStretch(0, 1)
        master_layout.setRowStretch(1, 1)

        master_layout.setColumnMinimumWidth(0, 900)
        master_layout.setColumnMinimumWidth(1, 450)
        master_layout.setRowMinimumHeight(1, 500)
        master_layout.addWidget(self.data_plt, 1, 0)
        master_layout.addWidget(self.hist_plt, 1, 1)
        master_layout.setColumnStretch(1, 0)

        button_grid_layout = QtWidgets.QGridLayout()
        button_grid_layout.addWidget(self.termination_button, 0, 1,
                                     alignment=QtCore.Qt.AlignRight)
        button_grid_layout.addWidget(self.save_csv_button, 0, 0,
                                     alignment=QtCore.Qt.AlignRight)
        button_grid = QtWidgets.QWidget()
        button_grid.setLayout(button_grid_layout)
        master_layout.addWidget(button_grid, 2, 1)
        master_layout.setRowStretch(2, 0)

        widget = QtWidgets.QWidget()
        widget.setLayout(master_layout)
        self.setCentralWidget(widget)

        self.show()

    def setup_plots(self):

        self.subplot_keys = list(self.plot_config_dict.keys())
        self.subplot_count = len(self.subplot_keys)

        self.data_plt = MplWidget(self, subplot_count=self.subplot_count)
        self.hist_plt = MplWidget(self, subplot_count=self.subplot_count)

        for i in range(self.subplot_count):

            subplot_key = self.subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            for topic in subplot_topics_list:
                self.data_plt.canvas.subplot_axes[i].plot(
                    self.data_df[self.x_axis_col], self.data_df[topic], label=topic)

                self.data_plt.canvas.subplot_axes[i].legend()

            sns.histplot(self.data_df[subplot_topics_list],
                         ax=self.hist_plt.canvas.subplot_axes[i], stat="probability")

            self.data_plt.canvas.subplot_axes[i].span = SpanSelector(
                self.data_plt.canvas.subplot_axes[i],
                onselect=self.on_region_select_callback,
                direction="horizontal",
                minspan=1,
                useblit=True,
                span_stays=False,
                button=[1],
                rectprops={"facecolor": "green", "alpha": 0.3})
        return

    def update_hist_plot(self, df):
        for i in range(self.subplot_count):
            self.hist_plt.canvas.subplot_axes[i].clear()
            subplot_key = self.subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            sns.histplot(df[subplot_topics_list],
                         ax=self.hist_plt.canvas.subplot_axes[i], stat="probability")
        self.hist_plt.canvas.draw()
        return

    def on_region_select_callback(self, min_x_val, max_x_val):
        self.data_plt.canvas.subplot_axes[0].set_xlim([min_x_val, max_x_val])
        cropped_df = self.crop_df(min_x_val, max_x_val)
        self.update_hist_plot(cropped_df)
        dialog_window = ConfirmSelectionWindow()
        selection_accepted = dialog_window.exec_()

        self.data_plt.canvas.subplot_axes[0].set_xlim(
            [self.x_start, self.x_end])
        self.data_plt.canvas.draw()
        self.update_hist_plot(self.data_df)

        if selection_accepted:
            print("selection accepted and added: ", min_x_val, max_x_val)
            cropped_df["old_index"] = copy.deepcopy(cropped_df.index)
            self.cropped_data_df = self.cropped_data_df.append(cropped_df)
            self.cropped_data_df = self.cropped_data_df.reset_index(drop=True)
            self.save_csv_button.setEnabled(True)

        return

    def crop_df(self, x_start, x_end):
        cropped_df = self.data_df[(self.x_axis_data >=
                                  x_start) & (self.x_axis_data <= x_end)]
        # cropped_df = cropped_df[]
        return cropped_df

    def _save_to_csv(self):

        file_dialog = QtWidgets.QFileDialog(self)
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        default_file_name = "output-" + timestr + ".csv"
        name = file_dialog.getSaveFileName(
            self, 'Save Dataframe to csv', default_file_name)
        file_path = name[0]
        if (file_path[-4:] != ".csv"):
            print("Wrong file name extension detected, adapting to *.csv")
            split_path = file_path.split(".", 1)
            file_path = split_path[0] + ".csv"
        print("Saving file to: ", file_path)
        self.cropped_data_df.to_csv(file_path, index=True)

        return

    def _terminate(self):
        self.close()
        return
