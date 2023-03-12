import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

def plot_candlestick_with_atr_msd(file_path, window_size, start_date, end_date):
    # Load data
    df = pd.read_csv(file_path)

    # Convert the 'Timestamp' column to a datetime object
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Set the index to the 'Timestamp' column
    df.set_index('Timestamp', inplace=True)

    # Calculate true range
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = np.abs(df['High'] - df['Close'].shift(1))
    df['L-PC'] = np.abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)

    # Calculate ATR
    n = 14
    df['ATR'] = df['TR'].rolling(n).apply(lambda x: ((n-1)*x[:-1].sum() + x[-1])/n, raw=True)

    # Calculate moving standard deviation
    df['Moving SD'] = df['Close'].rolling(window_size).std()

    # Filter data based on slicer date range
    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        if start_date not in df.index or end_date not in df.index:
            raise ValueError("Date range not in data.")
    except ValueError as e:
        print(e)
    
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
    ax2.plot(atr.index, atr.values, color='Blue', label='ATR')
    ax2.set_ylabel('ATR')
    ax2.legend()

    # Add Moving SD plot
    moving_sd = df_slice['Moving SD']
    ax3 = ax2.twinx()
    ax3.plot(moving_sd.index, moving_sd.values, color='Green',label='Moving Standard Deviation')
    ax3.set_ylabel('Moving SD')
    ax3.grid(False)
    ax3.legend()

    plt.xlabel('Date')
    plt.title('Candlestick Chart with ATR and Moving Standard Deviation')

    # Show plot
    plt.show()
