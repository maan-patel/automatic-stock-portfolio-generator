# import requests
# import datetime as dt
# import matplotlib.pyplot as plt
# from pandas_datareader import data as web
# import mplfinance as mpf
# import datetime as dt
#
#
# def portfolio_vis(stock_ticker, total_investment, risk):
#
#
#     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
#
#     querystring = {"region": "US", "symbols": stock_ticker}
#
#     headers = {
#         'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
#         'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     data = response.json()
#
#
#
#     url_recommender = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"
#
#     querystring_recommender = {"symbol": stock_ticker}
#
#     headers_recommender = {
#         'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
#         'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#     }
#
#     response_recommender = requests.request("GET", url_recommender, headers=headers_recommender,
#                                             params=querystring_recommender)
#
#     data_recommend = response_recommender.json()
#
#     total_recommendations = data_recommend['finance']['result'][0]['count']
#     tickers = []
#     prices = []
#     ticker_full_name = []
#
#     for i in range(total_recommendations):
#         tickers.append(data_recommend['finance']['result'][0]['quotes'][i]['symbol'])
#         ticker_full_name.append(data_recommend['finance']['result'][0]['quotes'][i]['shortName'])
#         prices.append(data_recommend['finance']['result'][0]['quotes'][i]['regularMarketPrice'])
#
#     # modify amounts to equal shares that equal to total_investment amount
#     total_amount = []
#     for i in range(len(tickers)):
#         total_amount.append((total_investment / prices[i]) / len(tickers))
#
#     amounts = [amount for amount in total_amount]
#
#     total = []
#
#     for i in range(len(tickers)):
#         total.append(prices[i] * amounts[i])
#
#
#     fig, ax = plt.subplots(figsize=(16, 8))
#
#     ax.set_facecolor('black')
#     ax.figure.set_facecolor('#121212')
#
#     ax.tick_params(axis='x', color='white')
#     ax.tick_params(axis='y', color='white')
#
#     ax.set_title('Stock Portfolio Recommendation Visualizer', color="#EF6C35", fontsize=20)
#
#     _, texts, _ = ax.pie(total, labels=tickers, autopct="%1.1f%%", pctdistance=0.8)
#     [text.set_color('white') for text in texts]
#
#     my_circle = plt.Circle((0, 0), 0.55, color="black")
#     plt.gca().add_artist(my_circle)
#
#     ax.text(-2, 1, 'Portfolio Overview', fontsize=14, color='#FFE536', verticalalignment='center',
#             horizontalalignment='center')
#     ax.text(-2, 0.85, f"Total USD Amount: ${sum(total):.2f}", fontsize=12, color='white', verticalalignment='center',
#             horizontalalignment='center')
#     counter = 0.15
#
#     for ticker in tickers:
#         ax.text(-2, 0.85 - counter, f'{ticker}: ${total[tickers.index(ticker)]:.2f}', fontsize=12, color='white',
#                 verticalalignment='center', horizontalalignment='center')
#         counter += 0.15
#
#     # return plt.savefig('portfolio.png')
#     return plt.show()
#
#
# if __name__ == "main":
#     portfolio_vis()
