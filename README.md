# panorama-frame - A Visual Dataframe Selector

The Visual Dataframe selector is a tool, that can be used to visually select numerical data from a pandas dataframe. This can be usefull for many applications like for example data selection for machine learning or system identification.

The tool is configurable in order to plot a range of dataframe columns in vertically stacked subplots.
Hereby the user can specify which columns are plotted in which subplot. Furthermore, a histogram is included to get a rough idea on the distribution of the data.

The user can subsequentially select different horizontal data windows via click and drag and he tool then automatically combines the visually selected sections into a new dataframe.

![visual_dataframe_selector(3)](https://github.com/manumerous/visual_dataframe_selector/assets/18735094/29fb830e-3272-418b-b74d-b19283b88fb0)

## Install dependencies

The use the visual pandas cropper you need to install python 3.8 and the needed python libraries. It is strongly advised to install the pip packages in a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) setup for this project, in orger to not interfere with other projects or system packages.

Install the dependencies from the project folder:

```
pip3 install -r requirements.txt
```

## Run the Visual Dataframe Selector

To run the programm you can import the function visual_pandas_selector(data_df, plot_config_dict) into your coding project. The format of the needed plot_config_dict can be seen in test_visual_pandas_cropper.py.

Alternatively you can test the tool with some reference data by running:

```
python3 test_panorama_frame.py
```

## Use the Tool

- Left click with your mouse and drag to define the desired horizontal window of the data to be selected.
  - The current selection distribution is now visualized in the histogram plot on the right.
- Confirm or cancel data selection.
  - The already selected data is now marked by a grey span in the plot on the left.
  - The plot on the right contains now the histogram of all selected data.
- repeat as many times as needed.
- Once you could select all desired horizontal data windows click "Done selecting"
