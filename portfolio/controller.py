import requests
# import mplfinance as mpf
import datetime as dt
# import requests
import urllib3
from decouple import config
from expertai.nlapi.cloud.client import ExpertAiClient
# import mpld3
# from mpld3 import plugins
# import yfinance as yf

# msft = yf.Ticker("MSFT")


# def api_call(stock_ticker):

#     stock = yf.Ticker(stock_ticker)
#     return stock.info['regularMarketPrice']

# print(api_call('AAPL'))

# 8a5cdbe10amshda1071659c3e749p104baajsn3f2f59f21a3a
# 3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3
# 1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e

 
def recommended_tickers(stock_ticker):


    url_recommender = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"

    querystring_recommender = {"symbol": stock_ticker}

    headers_recommender = {
        'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
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
        'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
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
        'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
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
        
def is_number_of_stocks(stock_ticker, investment_value):
    investment_arr = number_of_stocks(stock_ticker, investment_value)
    for i in investment_arr[0]:
        if i == 0:
            return False
    
    return True


def is_valid_graph(graph):
    graph_types = ['line', 'candle', 'bar']
    for i in graph_types:
        if i.lower() == graph.lower():
            return True
    return False

def number_for_graph(graph):
    graph_types = ['Candle', 'Line', 'Bar']
    for i, val in enumerate(graph_types):
        if graph.lower() == val.lower():
            return i + 1
    return 1
    


def sentiment_score(stock_ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/list"
    querystring = {"symbol":f"{stock_ticker}","messageBoardId":"finmb_24937","region":"US","userActivity":"true","sortBy":"createdAt","off":"0"}
    headers = {
        'x-rapidapi-key': "8a5cdbe10amshda1071659c3e749p104baajsn3f2f59f21a3a",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    # print(data)
    # print(data["canvassMessages"][0]["details"]["userText"])
    data_for_comments = data["canvassMessages"]
    EAI_USERNAME = config('EAI_USERNAME')
    EAI_PASSWORD = config('EAI_PASSWORD')
    import os
    os.environ["EAI_USERNAME"] = EAI_USERNAME
    os.environ["EAI_PASSWORD"] = EAI_PASSWORD
    
    client = ExpertAiClient()
    sum = 0
    count = 0
    text = ""
    for i in range(3):
        text += data_for_comments[i]["details"]["userText"]
    print(text)
    language= 'en'
        # print(text)
    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })
        # print(output.sentiment.overall)
        # print(text)
    sum = output.sentiment.overall
    
    # average = 0.0
    average = sum 
    return average



def search_drop_down(search_query):
    import json
    import requests

    url = f"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={search_query}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback"

    response = requests.get(url).text[39:-2]
    s = str(response)
    res = json.loads(s)
    data = res["ResultSet"]["Result"]
    result = []
    for i in range(len(data)):
        ticker = data[i]["symbol"]
        name = data[i]["name"]
        result.append(f'{ticker.upper()} - {name}')
    return result

def sentiment_for_news():
    import requests

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"

    querystring = {"region":"US","snippetCount":"28"}

    payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
    headers = {
        'content-type': "text/plain",
        'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    data = response.json()["data"]


    EAI_USERNAME = config('EAI_USERNAME')
    EAI_PASSWORD = config('EAI_PASSWORD')
    import os
    os.environ["EAI_USERNAME"] = EAI_USERNAME
    os.environ["EAI_PASSWORD"] = EAI_PASSWORD
    
    client = ExpertAiClient()
    sum = 0
    count = 0
    text = ""
    for i in range(10):
        text += data["main"]["stream"][i]["content"]["title"]
    # print(text)
    language= 'en'
        # print(text)
    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })
        # print(output.sentiment.overall)
        # print(text)
    sum = output.sentiment.overall
    
    # average = 0.0
    average = sum 
    # print(average)
    return average
    




# Testing for functions 
# print(sentiment_score("C"))

# print(is_number_of_stocks('AAPL', 1000))





# if __name__ == 'main':
#     graph()
#     portfolio_vis()