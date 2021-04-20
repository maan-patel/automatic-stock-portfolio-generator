import requests
import mplfinance as mpf
import datetime as dt
import mpld3
from mpld3 import plugins

# def graph(stock_ticker, date, type):
#     time = ["5y", "1y", "6m", "1m", "1w", "1d"]
#     type_chart = ['candle', 'line']
#     #
#     # while date not in time:
#     #     date = str(input(
#     #         'Invalid Input. Please enter "5y", "1y", "6m", "1m", "1w", "1d" to see the candle stick chart for the stock: '))
#     #
#     # while type not in type_chart:
#     #     type = str(input("Invalid Input. Please enter the type of graph you'd like to see (candle, line): ").lower())
#
#     if date == '5y':
#         start = dt.datetime(2016, 1, 1)
#     elif date == '1y':
#         start = dt.datetime(2020, 1, 1)
#     elif date == '6m':
#         start = dt.datetime(2020, 9, 1)
#     elif date == '1m':
#         start = dt.datetime(2021, 2, 1)
#     elif date == '1w':
#         start = dt.datetime(2021, 3, 1)
#     elif date == '1d':
#         start = dt.datetime(2021, 3, 30)
#
#     end = dt.datetime.now()
#     data = web.DataReader(stock_ticker, 'yahoo', start, end)
#
#     # plt.plot(data['Close'])
#     colors = mpf.make_marketcolors(up="#00ff00",
#                                    down="#ff0000",
#                                    wick="inherit",
#                                    edge='inherit',
#                                    volume='in')
#
#
#     style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
#
#
#
#
#     if type == 'candle':
#         candle = mpf.plot(data, type='candle', style=style, volume=True)
#         html_str = mpld3.fig_to_html(candle)
#         Html_file = open("graph.html", "w")
#         Html_file.write(html_str)
#         Html_file.close()
#
#         return candle
#
#     line = mpf.plot(data, type='line', style=style, volume=True, mav=(20, 40))
#     return line
#

def recommended_tickers(stock_ticker):


    url_recommender = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"

    querystring_recommender = {"symbol": stock_ticker}

    headers_recommender = {
        'x-rapidapi-key': "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response_recommender = requests.request("GET", url_recommender, headers=headers_recommender,
                                            params=querystring_recommender)

    data_recommend = response_recommender.json()

    total_recommendations = data_recommend['finance']['result'][0]['count']
    tickers = []
    ticker_full_name = []

    for i in range(total_recommendations):
        tickers.append(data_recommend['finance']['result'][0]['quotes'][i]['symbol'])
        ticker_full_name.append(data_recommend['finance']['result'][0]['quotes'][i]['shortName'])

    return tickers



#
# def portfolio_vis(stock_ticker, total_investment, risk):
#
#
#     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
#
#     querystring = {"region": "US", "symbols": stock_ticker}
#
#     headers = {
#         'x-rapidapi-key': "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
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
#         'x-rapidapi-key': "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
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
#     ax.set_facecolor('white')    #this
#     ax.figure.set_facecolor('#121212')
#
#     ax.tick_params(axis='x', color='black')
#     ax.tick_params(axis='y', color='black')
#
#     ax.set_title('Stock Portfolio Recommendation Visualizer', color="#EF6C35", fontsize=20)
#
#     _, texts, _ = ax.pie(total, labels=tickers, autopct="%1.1f%%", pctdistance=0.8)
#     [text.set_color('black') for text in texts]
#
#     my_circle = plt.Circle((0, 0), 0.55, color="white") #this
#
#     plt.gca().add_artist(my_circle)
#     fig.gca().add_artist(my_circle)
#
#     ax.text(-2, 1, 'Portfolio Overview', fontsize=14, color='#FFE536', verticalalignment='center',
#             horizontalalignment='center')
#     ax.text(-2, 0.85, f"Total USD Amount: ${sum(total):.2f}", fontsize=12, color='black', verticalalignment='center',
#             horizontalalignment='center')
#     counter = 0.15
#
#     for ticker in tickers:
#         ax.text(-2, 0.85 - counter, f'{ticker}: ${total[tickers.index(ticker)]:.2f}', fontsize=12, color='black',
#                 verticalalignment='center', horizontalalignment='center')
#         counter += 0.15
#
#     html_str = mpld3.fig_to_html(fig)
#     Html_file = open("fig.html", "w")
#     Html_file.write(html_str)
#     Html_file.close()
#
#
#     # hs = mpld3.save_html(plt, 'p.html')
#
#     # return mpld
#     # fig.savefig('../static/images/temp.png', dpi=fig.dpi)
#
#     # plt.savefig('temp.png')
#     return plt.savefig('temp.png')
#     # return plt.show()
#
# # portfolio_vis('CCL', 1000, 'high')
# # graph('CCL', '1m', 'candle')
#
#
#
# if __name__ == 'main':
#     graph()
#     portfolio_vis()