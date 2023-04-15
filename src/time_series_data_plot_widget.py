__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"

try:
    from src.dataframe_plot_widget import DataFramePlotWidget
except:
    from visual_dataframe_selector.src.dataframe_plot_widget import DataFramePlotWidget

from matplotlib.widgets import SpanSelector
import pandas as pd
from overrides import override


class TimeSeriesDataPlotWidget(DataFramePlotWidget):
    def __init__(self, plot_config_dict: dict, parentWindow):
        super(TimeSeriesDataPlotWidget, self).__init__(plot_config_dict, parentWindow)
        self.setup_span(parentWindow)

    def setup_span(self, parentWindow):
        for i in range(self.subplot_count):
            self.canvas.subplot_axes[i].span = SpanSelector(
                self.canvas.subplot_axes[i],
                onselect=parentWindow.on_region_select_callback,
                direction="horizontal",
                minspan=1,
                useblit=True,
                button=[1],
                props={"facecolor": "green", "alpha": 0.3},
            )

    @override
    def plot(self, df: pd.DataFrame):
        x_axis_data = df[self.x_axis_col]
        x_start = x_axis_data.iloc[0]
        x_end = x_axis_data.iloc[-1]
        self.canvas.subplot_axes[0].set_xlim([x_start, x_end])

        for i in range(self.subplot_count):
            subplot_key = self.subplot_keys[i]
            subplot_topics_list = self.plot_config_dict[subplot_key]
            for topic in subplot_topics_list:
                self.canvas.subplot_axes[i].plot(
                    df[self.x_axis_col], df[topic], label=topic
                )
                self.canvas.subplot_axes[i].legend(loc="lower right")

        self.canvas.draw()
        return

    def update_selection_visualitation(self, selection: dict):
        for subplot in self.canvas.subplot_axes:
            subplot.axvspan(
                selection["start"], selection["end"], facecolor="grey", alpha=0.3
            )
        self.canvas.draw()
        return
