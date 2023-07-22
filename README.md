# visual-pandas-curator

The Visual Pandas Curator is a tool to visually select portions of numeric time-series data from a pandas dataframe. The tool is intended to provide an fast interactive way for manual data selection, as can be very useful in for example machine learning, regression or system identification.

The tool is configurable in order to plot a range of dataframe columns in vertically stacked subplots.
Hereby the user can specify which columns are plotted in which subplot. Furthermore, a histogram is included to get a rough idea on the distribution of the data.

The user can subsequentially select different horizontal data windows via click and drag and he tool then automatically combines the visually selected sections into a new dataframe.

![visual_pandas_curator(3)](https://github.com/manumerous/visual_pandas_curator/assets/18735094/29fb830e-3272-418b-b74d-b19283b88fb0)

## Install dependencies

Install the dependencies from the top-level project folder using:

```bash
pip install .
```

## Include in your project

To include the visual-pandas-curator in your project you can import it using `import visual_pandas_curator`. Then simply use:

- If your project does not contain a pyqt application: `select_visual_data(data : pd.DataFrame, plot_config : dict)` 

- To add the visual-pandas-curator to an existing pyqt application: `select_visual_data_in_pyqt_app(data : pd.DataFrame, plot_config : dict, pyqt_app)` 


## Run the Example 

```bash
python3 visual_pandas_example.py
```

#### Use the Tool

- Left click with your mouse and drag to define the desired horizontal window of the data to be selected.
  - The current selection distribution is now visualized in the histogram plot on the right.
- Confirm or cancel data selection.
  - The already selected data is now marked by a grey span in the plot on the left.
  - The plot on the right contains now the histogram of all selected data.
- repeat as many times as needed.
- Once you could select all desired horizontal data windows click "Done selecting"
