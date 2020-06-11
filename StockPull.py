#will pull stock data (IEX probably)

from iexfinance.stocks import Stock

with open('IEX_Token.txt', 'r') as file:
    myfile = file.read()

a = Stock("AAPL", token=myfile)
a.get_quote()

