__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"

import pandas as pd
from pathlib import Path


try:
    from data_selector import select_visual_data
except:
    from visual_dataframe_selector.data_selector import select_visual_data


def test_visual_dataframe_selector():
    test_file_path = str(Path(__file__).parent.absolute()
                         ) + "/resources/test.csv"
    print(test_file_path)
    plot_config_dict = {
        "x_axis_col": "timestamp",
        "sub_plt1_data": ["q0", "q1", "q2", "q3"],
        "sub_plt2_data": ["u0", "u1", "u2", "u3", "u4", "u5", "u6", "u7"]}
    data_df = pd.read_csv(test_file_path, index_col=0)

    selected_df = select_visual_data(data_df, plot_config_dict)
    print("Selected dataframe:")
    print(selected_df)
    return


if __name__ == "__main__":
    test_visual_dataframe_selector()
