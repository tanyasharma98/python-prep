import requests
# r = requests.get("https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?period=quarter&limit=400&apikey=demo")
# print(r.text)
# print(r.status_code)


url = "http://www.facebook.com"
para = {
    "pq": 32,
    "wq": 23
}
r2 = requests.post(url=url, data=para)
print(r2.text)
