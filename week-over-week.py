#!/usr/bin/env python

import yfinance
import datetime

interesting = {
    'sp': yfinance.Ticker("SPY"), # S&P 500
    'dji': yfinance.Ticker("^DJI"), # DJIA
    'vix': yfinance.Ticker('^VIX'),
    'vtsax': yfinance.Ticker("VTSAX"),
}

end = datetime.datetime.today() - datetime.timedelta(days=1)
start = end - datetime.timedelta(weeks=1)

for symbol in interesting.keys():
    ticker = yfinance.Ticker(symbol)
    history = ticker.history(start=start, end=end)
    print("History for {}".format(symbol))
    print(history)
    print()
