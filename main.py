# from selenium import webdriver
import requests
import json

res=requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

#to print resp
# print(res)

# to print resp data
# print(res.json()["items"])


# to print resp data items
# print(res.json()["items"])


# to print specific data
# for data in res.json()["items"]:
#     print(data)
#     print(data['title'])
#     print(data['link'])
#     print()


# specific data
# for x in res.json()['items']:
#     if x['answer_count']==0:
#         print(x['title'])
#         print(x['link'])
#     else:
#         print('skipped..')
#     print()



