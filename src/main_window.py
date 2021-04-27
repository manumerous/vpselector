from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtCore, QtGui, QtWidgets
__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"

import sys
import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, subplot_count=1, dpi=100):
        fig = Figure(dpi=dpi)
        self.subplot_axes = []
        for i in range(subplot_count):
            curr_axes = fig.add_subplot(subplot_count, 1, i+1)
            self.subplot_axes.append(curr_axes)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data_df, plot_config_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.data_df = data_df

        # Prepare vertical col name and drop it from the plot config dict
        self.horizontal_axis_col = plot_config_dict["horizontal_axis_col"]
        self.plot_config_dict = plot_config_dict
        self.plot_config_dict.pop("horizontal_axis_col", None)

        plt = self.setup_plots()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(plt, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)

        layout.addWidget(plt)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def setup_plots(self):

        subplot_keys = list(self.plot_config_dict.keys())
        print(subplot_keys)
        subplot_count = len(subplot_keys)

        plt = MplCanvas(self, subplot_count=subplot_count, dpi=100)

        for i in range(subplot_count):
            subplot_key = subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            curr_axes = plt.subplot_axes[i]
            for topic in subplot_topics_list:
                curr_axes.plot(
                    self.data_df[self.horizontal_axis_col], self.data_df[topic], label=topic)
            curr_axes.legend()
        return plt
