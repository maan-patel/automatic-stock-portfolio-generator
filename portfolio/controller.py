import requests
from decouple import config
from expertai.nlapi.cloud.client import ExpertAiClient
import datetime as dt
import os
from functools import lru_cache, wraps

#Init env
# Take care of this boilerplate right upfront.
#0. Do this only ONCE. decouple will cache this from the configs
EAI_USERNAME = config("EAI_USERNAME")
EAI_PASSWORD = config("EAI_PASSWORD")
RAPI_NEWS_KEY  = config("x-rapidapi-key")
RAPI_NEWS_HOST = config("x-rapidapi-host")
os.environ["EAI_USERNAME"] = EAI_USERNAME
os.environ["EAI_PASSWORD"] = EAI_PASSWORD
NL=os.linesep #Platform independent newline
TEXT_LIMIT=10000


### 1. Decorators to log errors -- currently to stdout, apply logging as needed
def timefunc(func):
    #print(f"In timefunc({func}, args = {args}, kwargs = {kwargs}).") 
    ARGSZ_LIMIT = 10485760
    import pandas as pd
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        # NOTE: To prevent a "large" pandas object, ie,
        # one arbitrarily determined as > 10 MB, passed 
        # to the decorated function from ironically
        # freezing the timer decorator, we only print a 
        #.placeholder instead.
        argcopy = []
        for a in args:
            t = type(a)
            if t == pd.DataFrame or t == pd.Series:
                    sz, shape = a.size, a.shape
                    if sz > ARGSZ_LIMIT: 
                        print(f"Wrapper: DF of size {sz} exceeded output size limit of {ARGSZ_LIMIT}. Suppressing printing of args.")
                        argcopy.append('HUGE_DF!')
                        #noargsprint = True
                    else:
                        argcopy.append(f"DF: {a}")
            else:
                    argcopy.append(a)
                    #print(f"Wrapper: Encountered type {t} in args")

        tmp = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()

        args = tuple(argcopy) 
        print(f"function {func.__name__}({args}, {kwargs})  took {t2 - tmp} ns.")
        return result
    return wrapper

# 2. Reuse this code!!! DRY: Don't Repeat Yourself!!! Tired of this biolerplate strewn all over the code
@timefunc
def expert_api_client():
    return ExpertAiClient()
    """
    client is an opaque API handle -- gets a session 
    token from the Server, proxy/stub with no user 
    servicable parts, such as caching state and 
    checking liveness of the underlying network 
    connection.
    """

### 3. Use this decorator for all API calls will reduce the # of remote calls/TCP roundtrips
### and other overhead, speeding up performance 
### Will do something similar for calls to harvest news if time permits
@lru_cache(maxsize=256, typed=True)
@timefunc
def eai_api_call(text: str, client = None, lang: str = 'en', resource: str = 'sentiment'):
    if not client:
        client = expert_api_client()
                
    return client.specific_resource_analysis(
                body={"document": {"text": text}},
                params={"language": lang, "resource": resource},
    )


#Workhorse for logging
def get_ts():
    return dt.datetime.today().strftime('%Y%m%d_%H%M%S')


#Refactored: don't know if this function is even being used.
# @timefunc
def recommended_tickers(stock_ticker):
    """ Refactored: DRY! """
    url_recommender = (
        "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"
    )

    querystring_recommender = {"symbol": stock_ticker}

    headers_recommender = {
        "x-rapidapi-key": "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    }

    response_recommender = requests.request(
        "GET",
        url_recommender,
        headers=headers_recommender,
        params=querystring_recommender,
    )

    data_recommend = response_recommender.json()
    #### 4. SS refactoring: cache temporary results, don't keep accessing the same address over and over ####
    results = data_recommend["finance"]["result"][0] # SS

    total_recommendations = results["count"]
    tickers = []
    ticker_full_name = []

    # 5. Can use a compact listcomp here
    for i in range(total_recommendations):
        quote = results["quotes"][i]
        tickers.append(quote["symbol"])
        ticker_full_name.append(quote["shortName"])

    return tickers

# print(recommended_tickers("AAPL"))

# Tiny bit of repetition refactored.
@timefunc
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
        ref = data[i]
        ticker = ref["symbol"]
        #name = data[i]["name"]
        name = ref["name"]
        result.append(f"{ticker.upper()} - {name}")
    return result

# Finally, a function and API that really works! Caches all results. Add code to reuse this cache
# if you like. The file generated can even be uploaded to Mongo/Redis to serve news.
# And DO NOT forget to remove my API keys!!!
@lru_cache(maxsize=256, typed=True)
@timefunc
def sentiment_for_news2(symbols: set, output_file: str = None, summary_file: str = 'sentilent.log') -> list:
    import requests
    
    client = expert_api_client()

    language = "en"
    headers = {
        'x-rapidapi-key' : RAPI_NEWS_KEY,
        'x-rapidapi-host': RAPI_NEWS_HOST
    }

    nsyms = len(symbols)
    sents = {}
    lines = []
    save_data: bool = output_file is not None
    for p, symbol in enumerate(symbols,1):
        url = f"https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/{symbol}"
        print(f"Processing ticker #{p} of {nsyms}: {symbol}.")

        response = requests.request("GET", url, headers=headers)

        js = response.json()
        items = js.get('item', None)
        if not items:
            print(f"ticker #{p} of {nsyms}: No data items for ticker {symbol}?")
            continue

        totsent = 0.0

        for item in items:
            text = ". ".join([item['title'], item['description']])           
            textlen = len(text)
            print(f"Ticker #{p} of {nsyms}: Textlen = {textlen}.")
            if textlen > TEXT_LIMIT:
                print(f"Ticker #{p} of {nsyms}: Truncating text to {TEXT_LIMIT} chars for symbol {symbol} . . .")
                text = text[:TEXT_LIMIT]
            
            output = eai_api_call(text, client = client)
            sent = output.sentiment.overall
            totsent += sent
            sents[symbol] = (text, sent)
            lines.append("|".join([ get_ts(), symbol, str(sent), text ]))
                    
            ###print(f'Ticker #{p} of {nsyms}: symbol={symbol}, sentiment={sent}, news:{NL}"""{NL}{text}{NL}"""')

        #print(f'DEBUG: {p}. Total sentiment for symbol {symbol} is {totsent} for news{NL}"""{NL}{text}{NL}"""')
        lines.append(50 * "#")
        m = f'{p}. *** SENTIMENT SUMMARY ***|{get_ts()}|{symbol}|{totsent}'
        print(m, flush=True)        
        lines.append(m)
        lines.append(50 * "#")

        
    for k, v in sents.items():
        print(f'Ticker #{p} of {nsyms}: Symbol= {k}, score = {v[1]}, text = "{v[0]}".') 
    if save_data:
         if os.path.exists(output_file):
            src = output_file
            ts = get_ts().rstrip(':')
            dst = f"{ts}_{output_file}"
            print(f"Output file {output_file} already exists! Backing up to {dst} . . .")
            os.rename(src, dst)
         with open(output_file,'at+') as fp:
                 cdata = NL.join(lines)
                 print(cdata[:10])
                 print(cdata, file=fp, flush=True)
    return sents


def load_ticker_file(tfile: str = 'tickers') -> list :
    with open(tfile) as fp:
        return frozenset([ l.strip() for l in fp.readlines()])


def tickerfile_test():
    stocks = load_ticker_file()
    sentiment_for_news2(stocks, output_file='stock_pulse.out')

#Test run
# tickerfile_test()


#sentiment_for_news2(('MCO', 'BRK.A', 'BRK.B' "AAPL", "AMZN", 'MSFT', 'CRM', 'COUP', "GOOG", 'GOOGL', "IBM", 'XOM', 'MRNA', 'PFE', 'SNY', 'JNJ', 'AZN', 'REGN', 'EW', 'CVS', 'UNH', 'GILD', 'HUM', 'BSX', 'BIIB', 'MCK', 'MRK', 'AGIO', 'BMY', 'VNDA', 'OCGN', 'ARGX', 'ALNY', 'FATE', 'SAGE', 'INCY', 'APLS', 'SRPT', 'ABC', 'ABT', 'LLY', 'DHR', 'AMGN', 'ISRG', 'SYK', 'ABBV', 'TMO', 'CI', 'BDX', 'ANTM', 'ZTS', 'ILMN', 'VRTX', 'HCA', 'WBA', 'VEEV', 'NBIX', 'WMT', 'BRK.A', 'BRK.B' "AAPL", "AMZN", 'MSFT', 'CRM', 'COUP', "GOOG", 'GOOGL', "IBM", 'XOM'), output_file='stock_pulse.out')

#Functions not used ATM due to poor entrypoints with low quality results / bad APIs
@timefunc
def sentiment_for_news(num: int=0):
    import requests

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"

    querystring = {"region": "US", "snippetCount": "28"}

    payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
    headers = {
        "content-type": "text/plain",
        "x-rapidapi-key": "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring
    )
    data = response.json()["data"]
    datalen = len(data)
    if datalen <= 0:
        print("No news data returned")
        return
    print(f"DATALEN = {datalen}")
    data_used = data

    print(f"Datatype of data_used = {type(data_used)}.")

    #if 0 < num < datalen:
    #    data_used = data_used[:num]
    #    datalen = len(data_used)

    print(f'DEBUG: sentiment_for_news: news = """{NL}{data_used}{NL}"""')

    text = ""
    for i in range(datalen):
        t = data_used["main"]["stream"][i]["content"]["title"]
        print(f"Adding main/stream/{i}/content/title of '''{NL}{t}{NL}'''")
        #text += data_used["main"]["stream"][i]["content"]["title"]
        text += t
    # print(text)
    language = "en"
    # print(text)
    client = expert_api_client()
    output = eai_api_call(text, client=client)
    #output = client.specific_resource_analysis(
    #    body={"document": {"text": text}},
    #    params={"language": language, "resource": "sentiment"},
    #)
    # print(output.sentiment.overall)
    # print(text)
    sent = output.sentiment.overall
    print(f'DEBUG: sentiment_for_news is {sent} for news = """{NL}{data_used}{NL}"""')

    return sent

#sentiment_for_news()

@timefunc
def eval_stocks(stocks: dict):
    get_sentiment_scores(get_newsdata(stocks))


@timefunc
def get_sentiment_scores(news: dict):
    if len(news) <= 0:
        print("No stock news data to process.")
        return
    client = expert_api_client()
    scores = {}
    for ticker, item in news.items():
        num_comments = len(item)
        if num_comments <= 0:
            print(f"No news found for ticker {ticker}. Skipping . . .")
            continue
        text = "".join([item[i]["details"]["userText"] for i in range(num_comments)])
        print(f"Text = '''{NL}{text}{NL}'''")
        print(f"Calculating news sentiment for ticker {ticker}:{NL}text = '''{NL}{text}{NL}''' . . .")
        language = "en"
        # print(text)
        #output = client.specific_resource_analysis(
        #    body={"document": {"text": text}},
        #    params={"language": language, "resource": "sentiment"},
        #)
        output = eai_api_call(text, client=client)
        scores[ticker] = output.sentiment.overall
        #text = ""
    print("scores:", scores)
    return scores




#########################################################
# Testing for functions
###eval_stocks(("AAPL", "AMZN", "GOOG", "IBM"))
# for i, ticker in enumerate(('AAPL', 'AMZN', 'GOOG', 'IBM'), 1):
#    print(i, ticker, sentiment_score(ticker))


#    for stock_ticker in stock_tickers:
#        querystring = {"symbol":f"{stock_ticker}","messageBoardId":"finmb_24937","region":"US","userActivity":"true","sortBy":"createdAt","off":"0"}
#        response = requests.request("GET", url, headers=headers, params=querystring)
#########################################################


def recommended_stock_weight(stock_ticker):

    url_recommender = (
        "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"
    )

    querystring_recommender = {"symbol": stock_ticker}

    headers_recommender = {
        "x-rapidapi-key": "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    }

    response_recommender = requests.request(
        "GET",
        url_recommender,
        headers=headers_recommender,
        params=querystring_recommender,
    )

    data_recommend = response_recommender.json()

    results = data_recommend["finance"]["result"][0]
    total_recommendations = results["count"]
    tickers_prices = []

    for i in range(total_recommendations):
        tickers_prices.append(results["quotes"][i]["regularMarketPrice"])

    return tickers_prices


def is_valid_ticker(stock_ticker):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": stock_ticker}

    headers = {
        "x-rapidapi-key": "1ef84c9bc0msh0ec5f4323cd2733p19e01fjsn40a6d4d91c6e",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    if len(data["quoteResponse"]["result"]) == 0:
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
    graph_types = ["line", "candle", "bar"]
    for i in graph_types:
        if i.lower() == graph.lower():
            return True
    return False


def number_for_graph(graph):
    graph_types = ["Candle", "Line", "Bar"]
    for i, val in enumerate(graph_types):
        if graph.lower() == val.lower():
            return i + 1
    return 1

# if __name__ == 'main':
#     graph()
#     portfolio_vis()

