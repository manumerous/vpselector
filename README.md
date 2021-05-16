# Visual Dataframe Selector

The Visual pandas cropper is tool, that can be used to visually select numerical data from a pandas dataframe. This can be usefull for many applications like for example data selection for machine learning or system identification.

The tool is configurable in order to plot a range of dataframe columns in vertically stacked subplots.
Hereby the user can specify which columns are plotted in which subplot. Furthermore, a histogram is included to get a rough idea on the distribution of the data.

The user can subsequentially select different horizontal data windows via click and drag and he tool then automatically combines the visually selected sections into a new dataframe.

![Screenshot from 2021-05-02 19-40-25](https://user-images.githubusercontent.com/18735094/116822371-c2f50a80-ab7e-11eb-9f92-37e368873ef9.png)

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
python3 test_visual_pandas_selector.py
```

## Use the Tool

- Left click with your mouse and drag to define the desired horizontal window of the data to be selected
- Confirm or cancel data selection
- The view automatically resets to contain all data and you can select the next data snipplet.
- Once you could select all desired horizontal data windows click "done selecting"
