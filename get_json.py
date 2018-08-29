import json
from alpha_vantage.timeseries import TimeSeries
import constants
import pandas as pd

def get_data(time, tick):
    ts = TimeSeries(key='4H9RHI4W5JZIHA3Z', output_format='pandas')
    if time == constants.time['1d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='5min', outputsize='compact')
    elif time == constants.time['5d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='30min', outputsize='compact')
    elif time == constants.time['1m']:
        data,meta_data = ts.get_daily(symbol=tick, outputsize='compact')
    else:
        data, meta_data = ts.get_daily(symbol=tick, outputsize='full')
    data = data[::-1]
    return data, meta_data


if __name__ == '__main__':
    df = (get_data(constants.time['1y'], 'MSFT'))
    df = df[0].to_json(orient='table', date_format="iso")
    with open('data.json', 'w') as outfile:
        json.dump(df, outfile)

    