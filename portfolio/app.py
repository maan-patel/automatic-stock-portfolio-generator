# import requests
# from candlestick import graph
# # from API import api_request
#
# url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
#
# stock_ticker = input('Please enter a Stock Ticker: ').upper()
#
# querystring = {"region": "US", "symbols": stock_ticker}
#
# headers = {
#     'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
#     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# data = response.json()
#
# while (len(data['quoteResponse']['result'])) == 0:
#     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
#     stock_ticker = input('Please enter a valid Stock Ticker: ').upper()
#     querystring = {"region": "US", "symbols": stock_ticker}
#     headers = {
#         'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
#         'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#     }
#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)
#     data = response.json()
#     if (len(data['quoteResponse']['result'])) == 1:
#         # stock_ticker = input('Please enter a valid Stock Ticker: ').upper()
#         break
#
#
# date = str(input('Please enter "5y", "1y", "6m", "1m", "1w", "1d" to see the candle stick chart for the stock: ').lower())
# type = str(input(
#     "Please enter the type of graph you'd like to see (candle, line): ").lower())
#
# total_investment = int(
#     input('Please enter the amount of money you want to invest: $'))
#
# sector = str(input('What sector are you interested in?'))
# risk = str(input('What is your risk profile?'))
#
#
# # portfolio_vis(stock_ticker, total_investment, risk)
# #
# # graph(stock_ticker, date, type)
