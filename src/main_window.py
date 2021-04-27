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

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data_df, plot_config_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.data_df = data_df

        # Prepare vertical col name and drop it from the plot config dict
        self.horizontal_axis_col = plot_config_dict["horizontal_axis_col"]
        self.plot_config_dict = plot_config_dict
        self.plot_config_dict.pop("horizontal_axis_col", None)

        self.subplot_list = []

        for subplot_data_list in self.plot_config_dict.keys():
            subplot = self.setup_plot(
                self.plot_config_dict[subplot_data_list])
            self.subplot_list.append(subplot)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.subplot_list[0], self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)

        for subplot in self.subplot_list:
            layout.addWidget(subplot)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def setup_plot(self, topic_list):
        plt = MplCanvas(self, width=10, height=4, dpi=100)
        for topic in topic_list:
            plt.axes.plot(
                self.data_df[self.horizontal_axis_col], self.data_df[topic], label=topic)
        plt.axes.legend()
        return plt
