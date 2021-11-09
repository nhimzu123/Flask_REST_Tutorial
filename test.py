import re
import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 100, "name": "John Wick 3", "views": 1200},
    {"likes": 1100, "name": "Rurouni Kenshin", "views": 1244},
    {"likes": 400, "name": "Saving Private Ryan", "views": 1300}
]

# Add records to DB
# for i in range(len(data)):
#     respone = requests.put(BASE + "video/" + str(i), data=data[i])
#     print(respone.json())

response = requests.put(BASE + 'video/12', data={"likes": 2000, "name": "Chainos Solution and Friends", "views": 4000})
print(response.json())

# Get the record
# input()
# respone = requests.get(BASE + "/video/12")
# print(respone.json())


# Update the record
# input()
# response = requests.patch(BASE + 'video/2', {"views": 99})
# print(response.json())

# Delete a record
# response = requests.delete(BASE + "video/12")
# print(response.json())


# response = requests.get(BASE + 'video/12')
# print(response.json())