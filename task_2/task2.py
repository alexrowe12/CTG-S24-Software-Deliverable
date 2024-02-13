import yfinance as yf
import csv

# Creates list of tickers, same as task 1
tickerList = []
with open("tickers.txt", "r") as tickerListReader:
    tickerListReader = csv.reader(tickerListReader)
    for i in tickerListReader:
        tickerList.append(i)

# Factor 1: Price Momentum
for ticker in tickerList:
    pastPrices = []
    pm = 0
    pmList = []
    tickerName = (str(ticker))[2:-2]
    filePath = "data/" + tickerName + ".csv"

    # Opens file, sets to read mode
    with open(filePath, "r") as currFile:
        reader = csv.DictReader(currFile)

        # If pastPrices is not full, appends without popping
        # If pastPrices is full, pops the first item on the list and appends new rounded 
        #   prices to the end
        for row in reader:
            if (len(pastPrices) < 5):
                pastPrices.append(round(float(row["Close"]), 2))
            else:
                pastPrices.pop(0)
                pastPrices.append(round(float(row["Close"]), 2))
                pm = round(float(((pastPrices[4] - pastPrices[0]) / pastPrices[0]) * 100))
                pmList.append(pm)

    print(tickerName + ": " + str(pastPrices))
    print(tickerName + ": " + str(pmList))


            