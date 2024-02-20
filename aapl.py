import yfinance as yf
import matplotlib.pyplot as plt

#Define the ticker symbol for the stock
ticker_symbol ='AAPL'
#Get stock data
stock_data=yf.download(ticker_symbol, start='2023-01-01', end='2024-01-01')
#plkot the stock price chart
plt.figure(figsize =(10,6))
plt.plot(stock_data['Close'],label ='Close price')
plt.title(f'stock price Chart for {ticker_symbol}')
plt.xlabel('Date')
plt.ylabel('price (USD)')
plt.legend()
plt.grid(True)
plt.show()