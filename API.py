# import requests
# import json
#
#
# def api_request(url, stock_ticker):
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
# if __name__ == 'main':
#     api_request()