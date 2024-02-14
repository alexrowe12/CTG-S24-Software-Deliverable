import yfinance as yf
import csv
import pandas as pd

# Creates list of tickers, same as task 1
tickerList = []
with open("tickers.txt", "r") as tickerListReader:
    tickerListReader = csv.reader(tickerListReader)
    for i in tickerListReader:
        tickerList.append(i)

# Factor 1: Price Momentum

# Writing first line
tickerRow = ','.join([ticker[0] for ticker in tickerList])
tickerRow = "Date," + tickerRow
with open("task_2/priceMomentum.csv", "w", newline='') as pmFile:
    pmFile.write(tickerRow)

for ticker in tickerList:
    tickerNum = 0
    pastPrices = []
    pm = 0
    pmList = []
    tickerName = (str(ticker))[2:-2]
    filePath = "data/" + tickerName + ".csv"
    fileWritePath = "task_2/data/" + tickerName + ".csv"

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

        pd.DataFrame(pmList).to_csv(fileWritePath)


    # Attempt to write in the same format as sample-factor.csv, aborted
    # with open("task_1/priceMomentum.csv", 'w', newline="") as columnWriter:
    #     writer = csv.writer(columnWriter)
    #     with open(filePath, 'r') as columnReader:
    #         reader = csv.reader(columnReader, delimiter=',')
    #         for row in reader:  
    #             row[1] = columnReader.readline() 
    #             writer.writerow(row)

    # TODO: create function for Volume Adjusted Momentum