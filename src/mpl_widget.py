__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from PyQt5.QtWidgets import QVBoxLayout, QWidget


class MplWidget(QWidget):
    def __init__(self, parentWindow=None, subplot_count=1):
        QWidget.__init__(self, parentWindow)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.subplot_axes = []

        for i in range(subplot_count):
            if i == 0:
                ax1 = self.canvas.figure.add_subplot(subplot_count, 1, i + 1)
                self.canvas.subplot_axes.append(ax1)
            else:
                curr_ax = self.canvas.figure.add_subplot(
                    subplot_count, 1, i + 1, sharex=ax1
                )
                self.canvas.subplot_axes.append(curr_ax)

        self.setLayout(vertical_layout)
