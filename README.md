# Candlestick-Chart-with-ATR-and-MSD

**Step by Step Procedure**

1. Install the required libraries - pandas, numpy, matplotlib, and mplfinance. You can install them using pip or conda package manager.

2. Prepare your data file in CSV format with columns: Timestamp, Open, High, Low, and Close.

3. Save the data file in your project folder.

4. Import the necessary libraries by adding the following lines at the beginning of your Python file:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
```


5. Define the function plot_candlestick_with_atr_msd that takes four arguments: file_path, window_size, start_date, and end_date. The file_path argument should be the path to your data file, while window_size, start_date, and end_date are used to filter the data based on a specific date range.

6. Inside the plot_candlestick_with_atr_msd function, load your data file using pandas read_csv function and convert the 'Timestamp' column to a datetime object.

7. Set the 'Timestamp' column as the index of the data frame.

8. Calculate the true range, ATR, and moving standard deviation using the pandas rolling function.

9. Filter the data based on the slicer date range and create a candlestick chart using mplfinance candlestick_ohlc function. Add the ATR and moving standard deviation plot using matplotlib plot function.

10. Show the plot using matplotlib show function.

11. Call the plot_candlestick_with_atr_msd function with appropriate arguments to create the plot.

You can use the following code as an example to call the plot_candlestick_with_atr_msd function:

```python
plot_candlestick_with_atr_msd('data.csv', 30, '2021-01-01', '2022-01-01')
```

This will plot a candlestick chart with ATR and moving standard deviation for the data in the 'data.csv' file for the date range from January 1, 2021, to January 1, 2022, with a moving window size of 30.
