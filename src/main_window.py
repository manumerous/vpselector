
__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"

from src import ConfirmSelectionWindow
from src import MplWidget

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import SpanSelector


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data_df, plot_config_dict, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Visual Pandas Cropper")

        self.data_df = data_df

        # Prepare vertical col name and drop it from the plot config dict
        self.horizontal_axis_col = plot_config_dict["horizontal_axis_col"]
        self.plot_config_dict = plot_config_dict
        self.plot_config_dict.pop("horizontal_axis_col", None)

        self.setup_plots()

        # Create toolbar for simultaneous manipulation of all subplots
        self.addToolBar(NavigationToolbar(self.plt.canvas, self))
        # toolbar = NavigationToolbar(self.plt, self)

        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(toolbar)

        layout.addWidget(self.plt)

        # Create a placeholder widget to hold the toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def on_region_select_callback(self, min_val, max_val):
        print(min_val, max_val)
        dialog_window = ConfirmSelectionWindow()
        dialog_window.exec_()
        return

    def setup_plots(self):

        subplot_keys = list(self.plot_config_dict.keys())
        subplot_count = len(subplot_keys)

        self.plt = MplWidget(self, subplot_count=subplot_count)

        for i in range(subplot_count):

            subplot_key = subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            for topic in subplot_topics_list:
                self.plt.canvas.subplot_axes[i].plot(
                    self.data_df[self.horizontal_axis_col], self.data_df[topic], label=topic)

                self.plt.canvas.subplot_axes[i].legend()

        # for i in range(subplot_count):
        #     subplot_key = subplot_keys[i]
        #     subplot_topics_list = self.plot_config_dict[subplot_key]
        #     curr_axes = self.plt.subplot_axes[i]
        #     for topic in subplot_topics_list:
        #         curr_axes.plot(
        #             self.data_df[self.horizontal_axis_col], self.data_df[topic], label=topic)
        #     curr_axes.legend()

            self.plt.canvas.subplot_axes[i].span = SpanSelector(
                self.plt.canvas.subplot_axes[i],
                onselect=self.on_region_select_callback,
                direction="horizontal",
                minspan=1,
                useblit=True,
                span_stays=True,
                button=[1],
                rectprops={"facecolor": "green", "alpha": 0.3})

        self.plt.show
