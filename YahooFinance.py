# Import 2 packages yfinance and pandas
import yfinance as yf
import pandas as pd

# Select what ticker symbol. We will select Bitcoin (BTC)
ticker = "BTC-USD"

# Define the start & end dates
start_date = "2023-01-01"  # Two years ago from today
end_date = "2023-07-31"    # Today

# Use yfinance to fetch historical data for Bitcoin
btc_data = yf.download(ticker, start=start_date, end=end_date)


# Display the first few rows of the btc_data DataFrame
print(btc_data.head())



