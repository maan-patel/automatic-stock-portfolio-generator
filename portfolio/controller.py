import requests
# import mplfinance as mpf
import datetime as dt
# import mpld3
# from mpld3 import plugins




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



def recommended_stock_weight(stock_ticker):


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
    tickers_prices = []

    for i in range(total_recommendations):
        tickers_prices.append(data_recommend['finance']['result'][0]['quotes'][i]['regularMarketPrice'])
     
    return tickers_prices


def is_valid_ticker(stock_ticker):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": stock_ticker}

    headers = {
        'x-rapidapi-key': "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    if len(data['quoteResponse']['result']) == 0:
        return False
    return True

# print(recommended_stock_weight('AAPL'))





# if __name__ == 'main':
#     graph()
#     portfolio_vis()