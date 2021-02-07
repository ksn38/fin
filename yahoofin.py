import requests
import json
import pprint
from datetime import date
from datetime import timedelta
from collections import OrderedDict
from bs4 import BeautifulSoup as bs
import time
t1 = time.time()


# def ticks():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
#     t_dict = OrderedDict()
#
#     for i in ('GSPC', 'VIX', 'TNX'):
#         url = 'https://finance.yahoo.com/quote/^' + i
#         response = requests.get(url, headers=headers).text
#         response = requests.get(url, headers=headers).text
#         parsed_html = bs(response, 'lxml')
#         # t = parsed_html.find('td', {'data-test': 'PREV_CLOSE-value'}).text.replace(',', '')
#         t = parsed_html.find('span', {'data-reactid': '32'}).text.replace(',', '')
#         t_dict[i] = float(t)
#
#     return t_dict
#
# print(ticks())

from yahoo_fin.stock_info import tickers_sp500, get_data

list_tickers = tickers_sp500()
print(list_tickers)

dict = {}

for i in list_tickers:
    print(i)
    try:
        ticker_now = get_data(str(i), start_date="23/12/2020", end_date="28/12/2020", index_as_date=True, interval="1d")
        print(ticker_now.close[-1])
    except:
        pass

t2 = time.time()

print(t2 - t1)


# from yahoo_fin.stock_info import tickers_sp500, get_data
#
# list_tickers = tickers_sp500()
# print(list_tickers)
#
# dict = {}
#
# for i in list_tickers:
#     print(i)
#     if i not in {'BF.B', 'BRK.B', 'HWM'}:
#         try:
#             ticker_old = get_data(str(i), start_date="20/11/2015", end_date="25/11/2015", index_as_date = True, interval="1d")
#             # print(ticker_old.close[-1])
#             ticker_now = get_data(str(i), start_date="23/12/2020", end_date="28/12/2020", index_as_date=True, interval="1d")
#             # print(ticker_now.close[-1])
#             dict[ticker_now.ticker[-1]] = round((ticker_now.close[-1]/ticker_old.close[-1] - 1)*100, 2)
#             print(dict[ticker_now.ticker[-1]])
#         except AssertionError:
#             pass
#
# dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
# print(dict)

# ticker_now = get_data('BF.B', start_date="23/12/2020", end_date="28/12/2020", index_as_date=True, interval="1d")