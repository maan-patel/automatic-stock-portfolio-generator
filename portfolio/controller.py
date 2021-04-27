import requests
# import mplfinance as mpf
import datetime as dt
# import mpld3
# from mpld3 import plugins
# import yfinance as yf

# msft = yf.Ticker("MSFT")


# def api_call(stock_ticker):

#     stock = yf.Ticker(stock_ticker)
#     return stock.info['regularMarketPrice']

# print(api_call('AAPL'))


def recommended_tickers(stock_ticker):


    url_recommender = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"

    querystring_recommender = {"symbol": stock_ticker}

    headers_recommender = {
        'x-rapidapi-key': "8a5cdbe10amshda1071659c3e749p104baajsn3f2f59f21a3a",
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
        'x-rapidapi-key': "8a5cdbe10amshda1071659c3e749p104baajsn3f2f59f21a3a",
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
        'x-rapidapi-key': "8a5cdbe10amshda1071659c3e749p104baajsn3f2f59f21a3a",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    if len(data['quoteResponse']['result']) == 0:
        return False
    return True


def number_of_stocks(stock_ticker, investment_value):
    prices = recommended_stock_weight(stock_ticker)
    split_investment = investment_value // 5
    stock_investory = []

    total_price = investment_value

    for price in prices:
        if price > split_investment:
            stock_investory.append(0)
            total_price -= 0
        else:
            stock_investory.append(int(split_investment // price))
            total_price -= price * int(split_investment // price)


    return [stock_investory, int(total_price)]
        
    

print(number_of_stocks('AAPL', 1000))





# if __name__ == 'main':
#     graph()
#     portfolio_vis()