import yfinance as yf
import csv
import pandas as pd

# Creates list of tickers, same as task 1
tickerList = []
with open("tickers.txt", "r") as tickerListReader:
    tickerListReader = csv.reader(tickerListReader)
    for i in tickerListReader:
        tickerList.append(i)

# Factor 3: Moving Average Convergence Divergence (MACD)

# Writing first line, useful if single-file format was used for data
# tickerRow = ','.join([ticker[0] for ticker in tickerList])
# tickerRow = "Date," + tickerRow
# with open("task_2/volAdjMomentum.csv", "w", newline='') as macdFile:
#     macdFile.write(tickerRow)

for ticker in tickerList:
    # Declarations of file paths and ticker name
    tickerName = (str(ticker))[2:-2]
    filePath = "data/" + tickerName + ".csv"
    fileWritePathMACD = "task_2/MACD_data/" + tickerName + "_MACD.csv"
    fileWritePathSignal = "task_2/MACD_sig_data/" + tickerName + "_sma26.csv"
    fileWritePath12 = "task_2/sma12_data/" + tickerName + "_sma12.csv"
    fileWritePath26 = "task_2/sma26_data/" + tickerName + "_sma26.csv"

    # Declarations of lists to store temporary data for calculations
    pastPrices12 = []
    pastPrices26 = []
    sma26List = []
    sma12List = []
    macdList = []
    macdSignalList = []
    buyList = []

    # Declarations of variables to story results of calcuations
    sma12 = 0
    sma26 = 0
    macd = 0
    macdSignal = 0

    # Doesn't allow repeated buy signals from MACD
    positive = False

    # Opens file handler
    with open(filePath, "r") as currFile:
        reader = csv.DictReader(currFile)

        # Iterates through each row and runs calculations
        for row in reader:
            curr_price = round(float(row["Close"]), 2)
            pastPrices12.append(curr_price)
            pastPrices26.append(curr_price)

            # Calcuations for simple moving averages
            if len(pastPrices12) > 12:
                pastPrices12.pop(0)

            if len(pastPrices12) == 12:
                sma12 = round((sum(pastPrices12) / 12), 2)
                sma12List.append(sma12)

            if len(pastPrices26) > 26:
                pastPrices26.pop(0)

            if len(pastPrices26) == 26:
                sma26 = round((sum(pastPrices26) / 26), 2)
                sma26List.append(sma26)
                macd = round(sma12 - sma26, 2)
                macdList.append(macd)

            # Calculations for MACD signal line from MACD calculation above
            if len(macdList) > 9:
                macdList.pop(0)
            
            if len(macdList) == 9:
                macdSignal = round((sum(macdList) / 9), 2)
                macdSignalList.append(macdSignal)

            # Testing for buy signals
            if len(macdSignalList) >= 9 and len(macdList) >= 9:
                if (macd - macdSignal) >= 0 and (macdSignalList[-1] - macdList[-1]) < 0 and positive == False:
                    print("Buy triggered: " + tickerName + " at " + str(curr_price) 
                            + ", " + str(row["Date"]))
                    positive = True

                if (macd - macdSignal) < 0 and (macdSignalList[-1] - macdList[-1]) >= 0 and positive == True:
                    print("Sell triggered: " + tickerName + " at " + str(curr_price) 
                            + ", " + str(row["Date"]))
                    positive = False
            
        # Writing data to CSVs for debugging
        pd.DataFrame(sma12List).to_csv(fileWritePath12)
        pd.DataFrame(sma26List).to_csv(fileWritePath26)
        pd.DataFrame(macdSignalList).to_csv(fileWritePathSignal)
        pd.DataFrame(macdList).to_csv(fileWritePathMACD)