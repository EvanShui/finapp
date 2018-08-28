""" Constants used throughout the project
"""

marketwatch_url = "http://www.marketwatch.com/search?q={ticker}&m=Ticker&rpp=15&mp=2005&bd=true&bd=false&bdv={month}%2F{day}%2F{year}&rs=true"
time = {
    '1d': 1,  # 5 minute intervals (need 78 points of data (compact))
    '5d': 2,  # 30 minute intervals (need 65 points of data (compact))
    '1m': 3,  # 1 day intervals (need ~30 points of data)
    '6m': 4,  # 1 day intervals (need ~180 points of data)
    'ytd': 5, # 1 day intervals (varies, hard stop at Jan)
    '1y': 6,  # 1 day intervals (~365 points of data)
    '5y': 7,  # 1 day interavls (need ~1825 points of data )
    'max': 8  # 1 day intervals (all lol)
}

yahoo_bio_url = "https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch"