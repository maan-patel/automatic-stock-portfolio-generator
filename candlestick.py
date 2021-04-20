# from pandas_datareader import data as web
# import mplfinance as mpf
# import datetime as dt
#
# def graph(stock_ticker, date, type):
#     time = ["5y", "1y", "6m", "1m", "1w", "1d"]
#     type_chart = ['candle', 'line']
#
#     while date not in time:
#         date = str(input(
#             'Invalid Input. Please enter "5y", "1y", "6m", "1m", "1w", "1d" to see the candle stick chart for the stock: '))
#
#     while type not in type_chart:
#         type = str(input("Invalid Input. Please enter the type of graph you'd like to see (candle, line): ").lower())
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
#         return candle
#
#     line = mpf.plot(data, type='line', style=style, volume=True, mav=(20, 40))
#     return line
#
# if __name__ == 'main':
#     graph()