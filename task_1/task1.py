import yfinance as yf
import csv

tickerList = []

# Opens and reads each line of the tickers.txt file, saving to tickerList
with open("tickers.txt", "r") as tickerListReader:
    tickerListReader = csv.reader(tickerListReader)
    for i in tickerListReader:
        tickerList.append(i)

# Creates a new csv file for each ticker in the tickerList, and writes data to it
for ticker in tickerList:

    tickerName = (str(ticker))[2:-2]
    currTickerObj = yf.Ticker(tickerName)

    # Writes to a new CSV file named after the ticker
    with open(("task_1/data/" + tickerName + ".csv"), "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)

        data = yf.download(ticker)

        csvWriter.writerow(data)

