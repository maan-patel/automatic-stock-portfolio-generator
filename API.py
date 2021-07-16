# import requests
# import urllib3
# from decouple import config

# url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/list"

# querystring = {"symbol":"BIIB","messageBoardId":"finmb_24937","region":"US","userActivity":"true","sortBy":"createdAt","off":"0"}

# headers = {
#     'x-rapidapi-key': "3b5eefa820msha0498f1c4c42783p194c3cjsnb6c5e4bc24a3",
#     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# data = response.json()
# # print(data)
# # print(data["canvassMessages"][0]["details"]["userText"])
# data_for_comments = data["canvassMessages"]



# # API_KEY_FOR_EXPERT_AI = "eyJraWQiOiI1RDVOdFM1UHJBajVlSlVOK1RraXVEZE15WWVMMFJQZ3RaUDJGTlhESHpzPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206Y291bnRyeSI6IkNBIiwic3ViIjoiZjY5M2YyMGItYmY2Yi00OTc3LWFjYWMtMGM3YjVmMjhhOGVjIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImN1c3RvbTpwZXJzb25hbGl6YXRpb25BdXRoIjoiMSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbVwvZXUtd2VzdC0xX0FVSGdRMDhDQiIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJmNjkzZjIwYi1iZjZiLTQ5NzctYWNhYy0wYzdiNWYyOGE4ZWMiLCJjdXN0b206Y29tcGFueSI6IlN0dWRlbnQiLCJhdWQiOiIxZWdzNjNxOTlwM3NlYmVjaHNiNzI5dDgwbyIsImV2ZW50X2lkIjoiZmYzZThlMGMtZmNhZC00OWQyLThkZmQtZTY0ZGEzNGNlMDFmIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjMxNzE3NjIsIm5hbWUiOiJNYWFuIiwicGhvbmVfbnVtYmVyIjoiKzE0MTY4ODkxNDE4IiwiZXhwIjoxNjIzMjU4MTYyLCJpYXQiOjE2MjMxNzE3NjIsImZhbWlseV9uYW1lIjoiUGF0ZWwiLCJlbWFpbCI6InBhdGVsLm1hYW4xNEBnbWFpbC5jb20iLCJjdXN0b206bWFya2V0aW5nQXV0aCI6IjEifQ.iVTjK0TkTyD7sE9vn3RxgOqLHm4qxvymehAtwx0-Oz73WiEqbuK0q-NmTLVBXpri4BuKziBf0MZFuJDFWRlOdxsJ4BJgGX6RFu8aBWLWSkltyJtiuJTEQNVcoTlzmVe6jHn1ezMgDjmHrU2Xhu0nm9ZeEI7TRzpmKjTx3d7_zGZcQ4sUOZPImmv3kGHBfuYrOLsXqTZtiCuw5P6p-JEJS7dc38EcR-57y07tgyF15zatMdjzXXwXBLkXA_5S40DOuFwVIf_NDEGwlWiJFF0piZ-Q-i_LYYGAlNbfx6mqXbPjkZjMO5HAHa-JyCZ_0dz0FPMXMj1OsuCSVx-4EwkmOA"


# EAI_USERNAME = config('EAI_USERNAME')
# EAI_PASSWORD = config('EAI_PASSWORD')

# import os
# os.environ["EAI_USERNAME"] = EAI_USERNAME
# os.environ["EAI_PASSWORD"] = EAI_PASSWORD

# from expertai.nlapi.cloud.client import ExpertAiClient
# client = ExpertAiClient()

# def sentiment_score(data_for_comments):
#     sum = 0
#     count = 0
#     for i in range(len(data_for_comments)):
#         text = data_for_comments[i]["details"]["userText"]
#         language= 'en'
#         # print(text)
#         output = client.specific_resource_analysis(
#             body={"document": {"text": text}}, 
#             params={'language': language, 'resource': 'sentiment'
#         })
#         print(output.sentiment.overall)
#         print(text)
#         sum += output.sentiment.overall
#         count += 1
    
#     average = 0.0
#     average = sum / count
#     return average

from yahoo_fin import news
 
new = news.get_yf_rss("nflx")
print(new)
# print(sentiment_score(data_for_comments))


# def search_drop_down(search_query):
#     import json
#     import requests

#     url = f"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={search_query}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback"

#     response = requests.get(url).text[39:-2]
#     s = str(response)
#     res = json.loads(s)
#     data = res["ResultSet"]["Result"]
#     result = []
#     for i in range(len(data)):
#         ticker = data[i]["symbol"]
#         name = data[i]["name"]
#         result.append(f'{ticker.upper()} - {name}')
#     return result


# print(search_drop_down('GO'))
