import requests

# params = {
# 'Accept': 'application/json, text/plain, */*',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language':"ru-RU,ru;q=0.9,cs-CZ;q=0.8,cs;q=0.7,en-US;q=0.6,en;q=0.5",
# 'Connection': 'keep-alive',
# 'Content-Length': '215',
# 'Content-Type': 'application/json',
# 'Cookie': 'LANG_SITE=ru; _ga=GA1.2.1279222753.1637851661; _gid=GA1.2.1147265934.1637851661; _gat_UA-129796047-1=1; _ym_uid=1637851661328976580; _ym_d=1637851661; _ym_visorc=w; _ym_isad=2; JSESSIONID=9F44A2933E83A4D8DA0B06C4BBE0F54F',
# 'DNT': '1',
# 'Host': 'ticket.rzd.ru',
# 'Origin': 'https://ticket.rzd.ru',
# 'Referer': 'https://ticket.rzd.ru/searchresults/v/1/5a323c29340c7441a0a556bb/5a13bd41340c745ca1e88b55/2022-01-24',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': "macOS",
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
# }
# r = requests.post('https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/TrainPricing?service_provider=B2B_RZD',headers=params)
#
# print(r)
# print(1)
r = requests.get('https://www.onetwotrip.com/_api/rzd/metaTimetable?adults=1&children=0&infants=0&date=01012022&from=22823&to=22871&isReturn=false&referrer_mrk=google.com%7C%2Fru%2Flandings').json()

print(r["result"][0])
cost = r["result"][0]["places"][0]["cost"]
start = r["result"][0]["from"]["metaName"]
finish = r["result"][0]["to"]["metaName"]
time_start = r["result"][0]["departure"]["isoTime"]
link = r["result"][0]["deeplink"]
print(cost)
print(start)
print(finish)
print(time_start)
print(link)

while True:
    print(1)