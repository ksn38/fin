import requests
import json
import pprint
from datetime import date
from datetime import timedelta
from collections import OrderedDict
from bs4 import BeautifulSoup as bs
import time

from test2 import x

import requests
from yahoo_fin.stock_info import tickers_sp500, get_data

list_tickers = tickers_sp500()

for i in list_tickers:
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + i + '?period1=1262304000&period2=1612656000&interval=1d&events=history&includeAdjustedClose=true'
    r = requests.get(url, allow_redirects=True)
    open('E:\\Temp\\sp500\\' + i + '.json', 'wb').write(r.content)