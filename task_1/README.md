Interpreting/accessing data:
- Data for each ticker is stored in a CSV file named [ticker].csv
- The header lists the columns of the CSV in order, being Date, Open, High, Low, Close, Volume
- Data can be accessed using a CSV reader from the Python CSV library
- row[column name] can be used to access data from a specific location, where row is the row number
    and column name is the name of the column that the user is trying to gain access to.

Issues encountered:
- Was unable to use command palette to create a virtual environment
    - Deactivated conda, reinstalled Homebrew, Pip, and Python, and created Venv from terminal
- tickerName was returning the full list item, including brackets and quotes
    - I used a slice of the string to take off the first two and last two characters
- Couldn't figure out why files were not able to be found
    - Used Python OS library to print current working directory with os.getcwd() and navigated from there