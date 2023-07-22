__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"


from visual_pandas_curator.widgets.mpl_widget import MplWidget

from abc import abstractmethod
import pandas as pd
import copy


class DataFramePlotWidget(MplWidget):
    def __init__(self, plot_config_dict, parentWindow):
        self.plot_config_dict = copy.deepcopy(plot_config_dict)
        self.x_axis_col = self.plot_config_dict["x_axis_col"]
        self.plot_config_dict.pop("x_axis_col", None)

        self.subplot_keys = list(self.plot_config_dict.keys())
        self.subplot_count = len(self.subplot_keys)

        super(DataFramePlotWidget, self).__init__(parentWindow, self.subplot_count)

    @abstractmethod
    def plot(self, df: pd.DataFrame):
        """Visualize the data from df in each subplot according to the specified columns in self.plot_config_dict."""
        pass
