
[![PyPI - Version](https://badge.fury.io/py/vpselector.svg)](https://pypi.org/project/vpselector/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/vpselector)](https://pypi.org/project/vpselector/)
[![CI Pipeline](https://github.com/manumerous/vpselector/actions/workflows/check_style.yaml/badge.svg)](https://github.com/manumerous/vpselector/actions/workflows/check_style.yaml)

# vpselector

The Visual Pandas Selector is a tool to visually select portions of numeric time-series data from a pandas dataframe. The tool is intended to provide an fast interactive way for manual data selection, as can be very useful in for example machine learning, regression or system identification.

Easily configure the tool to plot dataframe columns in vertically stacked subplots and view data distributions with the included histogram feature. With a simple click and drag, you can then select horizontal data windows, and let the tool automatically combine them into a new dataframe.

The user can subsequentially select different horizontal data windows via click and drag and he tool then automatically combines the visually selected sections into a new dataframe.

![ezgif com-gif-maker(1)](https://github.com/manumerous/visual-pandas-curator/assets/18735094/b5ebbb99-d2f7-4901-b101-cbeed6c230aa)


## Install

You can directly install the package in your terminal from [pypi.org](https://pypi.org/project/vpselector/) using:

```bash
pip install vpselector
```

## Use in your project

Then simply import it using `import vpselector`. Then simply use:

- If your project does not contain a pyqt application: `vpselector.select_visual_data(data : pd.DataFrame, plot_config : dict)` 

- To add the vpselector to an existing pyqt application: `vpselector.select_visual_data_in_pyqt_app(data : pd.DataFrame, plot_config : dict, pyqt_app)` 


## Run the Example 

```bash
python3 vpselector_example.py
```

#### Use the Tool

- Left click with your mouse and drag to define the desired horizontal window of the data to be selected.
  - The current selection distribution is now visualized in the histogram plot on the right.
- Confirm or cancel data selection.
  - The already selected data is now marked by a grey span in the plot on the left.
  - The plot on the right contains now the histogram of all selected data.
- repeat as many times as needed.
- Once you could select all desired horizontal data windows click "Done selecting"
