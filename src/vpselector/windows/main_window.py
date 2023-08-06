__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"


from vpselector.windows.confirm_selection_window import ConfirmSelectionWindow
from vpselector.widgets.time_series_data_plot_widget import TimeSeriesDataPlotWidget
from vpselector.widgets.histogram_plot_widget import HistogramPlotWidget

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QPushButton
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import pandas as pd
import time
import copy

pd.set_option("mode.chained_assignment", None)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, data : pd.DataFrame , plot_config : dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Visual Pandas Selector")

        self.data = data
        self.cropped_data = pd.DataFrame()
        # list of selected tuples (start_index, end_index)
        self.selection_list = []

        self.x_axis_data = self.data[plot_config["x_axis_col"]]

        self.data_plt = TimeSeriesDataPlotWidget(plot_config, parentWindow=self)
        self.data_plt.plot(self.data)
        self.hist_plt = HistogramPlotWidget(plot_config, parentWindow=self)

        # Create toolbar for simultaneous manipulation of all subplots
        self.addToolBar(NavigationToolbar(self.data_plt.canvas, self))

        master_layout = QtWidgets.QGridLayout()

        self.termination_button = QPushButton("Done selecting")
        self.termination_button.setFixedSize(150, 30)
        # connect signal
        self.termination_button.clicked.connect(self._terminate)

        self.save_csv_button = QPushButton("Save Result")
        self.save_csv_button.setFixedSize(150, 30)
        self.save_csv_button.setEnabled(False)
        # connect signal
        self.save_csv_button.clicked.connect(self._save_to_csv)

        master_layout.setColumnMinimumWidth(0, 900)
        master_layout.setRowMinimumHeight(2, 500)

        self.time_series_plot_label = QLabel(
            "Click and drag to select data using the mouse."
        )
        self.time_series_plot_label.setFixedHeight(50)
        self.hist_plot_label = QLabel("Histogram of all selected data.")
        master_layout.addWidget(self.time_series_plot_label, 1, 0)
        master_layout.addWidget(self.hist_plot_label, 1, 1)
        master_layout.addWidget(self.data_plt, 2, 0)
        master_layout.addWidget(self.hist_plt, 2, 1)
        master_layout.setColumnStretch(1, 0)

        button_grid_layout = QtWidgets.QGridLayout()
        button_grid_layout.addWidget(
            self.termination_button, 0, 1, alignment=QtCore.Qt.AlignRight
        )
        button_grid_layout.addWidget(
            self.save_csv_button, 0, 0, alignment=QtCore.Qt.AlignRight
        )
        button_grid = QtWidgets.QWidget()
        button_grid.setLayout(button_grid_layout)
        master_layout.addWidget(button_grid, 3, 1)
        master_layout.setRowStretch(2, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(master_layout)
        self.setCentralWidget(widget)

        self.show()

    def on_region_select_callback(self, min_x_val : int, max_x_val : int):
        cropped_df = self.crop_df(min_x_val, max_x_val)
        self.hist_plot_label.setText("Histogram of currently selected data.")
        self.hist_plt.plot(cropped_df)
        dialog_window = ConfirmSelectionWindow()
        selection_accepted = dialog_window.exec_()

        if selection_accepted:
            print("selection accepted and added: ", min_x_val, max_x_val)
            self.selection_list.append({"start": min_x_val, "end": max_x_val})
            cropped_df["old_index"] = copy.deepcopy(cropped_df.index)
            self.cropped_data = pd.concat([self.cropped_data, cropped_df])
            self.cropped_data = self.cropped_data.reset_index(drop=True)
            self.save_csv_button.setEnabled(True)
            self.data_plt.update_selection_visualitation(self.selection_list[-1])
        if self.cropped_data.empty:
            self.hist_plt.clear()
        else:
            self.hist_plt.plot(self.cropped_data)
        self.hist_plot_label.setText("Histogram of all selected data.")

        return

    def crop_df(self, x_start : int, x_end : int):
        cropped_df = self.data[
            (self.x_axis_data >= x_start) & (self.x_axis_data <= x_end)
        ]
        return cropped_df

    def _save_to_csv(self):
        file_dialog = QtWidgets.QFileDialog(self)
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        default_file_name = "output-" + timestr + ".csv"
        name = file_dialog.getSaveFileName(
            self, "Save Dataframe to csv", default_file_name
        )
        file_path = name[0]
        if file_path[-4:] != ".csv":
            print("Wrong file name extension detected, adapting to *.csv")
            split_path = file_path.split(".", 1)
            file_path = split_path[0] + ".csv"
        print("Saving file to: ", file_path)
        self.cropped_data.to_csv(file_path, index=True)

        return

    def _terminate(self):
        self.close()
        return
