import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates


df = pd.read_csv("C:/Users/Asus/Documents/Candlestick-Chart-with-ATR-and-MSD/Data/CL Data.csv")

# Convert the 'Timestamp' column to a datetime object
df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# Set the index to the 'Timestamp' column
df.set_index('Timestamp', inplace=True)


# calculate true range
df['H-L'] = df['High'] - df['Low']
df['H-PC'] = np.abs(df['High'] - df['Close'].shift(1))
df['L-PC'] = np.abs(df['Low'] - df['Close'].shift(1))
df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)

# calculate ATR
n = 14
df['ATR'] = df['TR'].rolling(n).apply(lambda x: ((n-1)*x[:-1].sum() + x[-1])/n, raw=True)


#Calculate MSD
# get user input for window size
window_size = int(input("Enter window size for moving standard deviation: "))

# calculate moving standard deviation using rolling function
df["Moving SD"] = df["Close"].rolling(window_size).std()
df = pd.read_csv("C:/Users/Asus/Documents/Candlestick-Chart-with-ATR-and-MSD/Data/CL Data.csv")

# Convert the 'Timestamp' column to a datetime object
df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# Set the index to the 'Timestamp' column
df.set_index('Timestamp', inplace=True)


# calculate true range
df['H-L'] = df['High'] - df['Low']
df['H-PC'] = np.abs(df['High'] - df['Close'].shift(1))
df['L-PC'] = np.abs(df['Low'] - df['Close'].shift(1))
df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)

# calculate ATR
n = 14
df['ATR'] = df['TR'].rolling(n).apply(lambda x: ((n-1)*x[:-1].sum() + x[-1])/n, raw=True)


#Calculate MSD
# get user input for window size
window_size = int(input("Enter window size for moving standard deviation: "))

# calculate moving standard deviation using rolling function
df["Moving SD"] = df["Close"].rolling(window_size).std()


# Add a slicer for adjusting the date range
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
try:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    if start_date not in df.index or end_date not in df.index:
        raise ValueError("Date range not in data.")
except ValueError as e:
    print(e)

# Filter data based on slicer date range
df_slice = df.loc[start_date:end_date]

# Create candlestick chart
ohlc = df_slice[['Open', 'High', 'Low', 'Close']]
ohlc.reset_index(inplace=True)
ohlc['Timestamp'] = ohlc['Timestamp'].apply(mdates.date2num)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8))
candlestick_ohlc(ax1, ohlc.values, width=0.6, colorup='green', colordown='red')
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')


# Add ATR plot
atr = df_slice['ATR']
ax2.plot(atr.index, atr.values)
ax2.set_ylabel('ATR')
ax2.set_title('Average True Range')

# Add Moving SD plot
moving_sd = df_slice['Moving SD']
ax3 = ax1.twinx()
ax3.plot(moving_sd.index, moving_sd.values, color='Blue')
ax3.set_ylabel('Moving SD')
ax3.grid(False)

plt.xlabel('Date')
plt.title('Candlestick Chart with ATR and Moving Standard Deviation')
# Show plot
plt.show()
