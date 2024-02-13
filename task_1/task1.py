import yfinance as yf
import csv

tickerList = []

# Opens and reads each line of the tickers.txt file, saving to tickerList
with open("tickers.txt", "r") as tickerListReader:
    tickerListReader = csv.reader(tickerListReader)
    for i in tickerListReader:
        tickerList.append(i)

# Iterates for each ticker, takes historial data, and uses .to_csv method to write to CSV
for ticker in tickerList:
    tickerName = (str(ticker))[2:-2]
    filePath = "data/" + tickerName + ".csv"
    tickerObj = yf.Ticker(tickerName)
    data = tickerObj.history(start="2022-01-01", end="2023-12-31", interval="1d", actions=False)
    data.to_csv(filePath)