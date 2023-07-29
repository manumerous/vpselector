__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"

from vpselector.widgets.dataframe_plot_widget import DataFramePlotWidget

import seaborn as sns
import pandas as pd
from overrides import override


class HistogramPlotWidget(DataFramePlotWidget):
    def __init__(self, plot_config: dict, parentWindow):
        super(HistogramPlotWidget, self).__init__(plot_config, parentWindow)

    @override
    def plot(self, df: pd.DataFrame):
        for i in range(self.subplot_count):
            self.canvas.subplot_axes[i].clear()
            subplot_key = self.subplot_keys[i]
            subplot_topics_list = self.plot_config[subplot_key]
            sns.histplot(
                df[subplot_topics_list],
                ax=self.canvas.subplot_axes[i],
                stat="probability",
            )

        self.canvas.draw()
        return

    def clear(self):
        for i in range(self.subplot_count):
            self.canvas.subplot_axes[i].clear()
        self.canvas.draw()
        return
