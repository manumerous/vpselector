# Visual Dataframe Selector

The Visual pandas cropper is tool, that can be used to visually select numerical data from a pandas dataframe. For example if the dataframe contains temporally ordered data it is possible to select multiple time windows out of the original frame. The tool then automatically combines the visually selected time windows to a new dataframe. 

![image](https://user-images.githubusercontent.com/18735094/116285521-7a101100-a78e-11eb-99fa-97dd5074690d.png)


## Install dependencies

The use the visual pandas cropper you need to install python 3.8 and the needed python libraries. It is strongly advised to install the pip packages in a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) setup for this project, in orger to not interfere with other projects or system packages.

Install the dependencies from the project folder:

```
pip3 install -r requirements.txt
```

## Run the Visual Dataframe Selector

To run the programm you can import the function visual_pandas_cropper(data_df, plot_config_dict) into your coding project. The format of the needed plot_config_dict can be seen in test_visual_pandas_cropper.py.

Alternatively you can test the tool with some reference data by running:


```
python3 test_visual_pandas_cropper.py
```

## Use the Tool
- Left click with your mouse and drag to define the desired horizontal window of the data to be selected
- Confirm or cancel data selection
- Click somewhere in the plot to reset to original view (should be automated in the future)
- Once you could select all desired horizontal data windows click "done selecting"
