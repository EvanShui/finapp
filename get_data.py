from alpha_vantage.timeseries import TimeSeries
import constants
import json
import pandas as pd
import datetime
from dateutil.rrule import *
import re

def read_json():
    with open('data.json', 'r') as infile:
        data = json.load(infile)
        df = pd.read_json(data, orient='table')
    return df

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
    return data,meta_data


def year_to_date(df):
    most_recent_date = df.iloc[0, :].name
    print(most_recent_date)
    current_year = str(most_recent_date.year)
    val_lst = df.index.values
    for index, date in enumerate(val_lst):
        date = str(date)[:10]
        if not (re.findall(current_year, date)):
            print(index)
            break
    return df.iloc[:index, :]    
   

def splice_data(df, time):
    if time==constants.time['1d']:
        df = df.iloc[:78, :]
    elif time==constants.time['5d']:
        df = df.iloc[:80, :]
    elif time==constants.time['1m']:
        df = df.iloc[:30, :]
    elif time==constants.time['6m']:
        df = df.iloc[:180, :]
    elif time==constants.time['ytd']:
        df = year_to_date(df)
        '''
        beginning_date = datetime.datetime.strptime(beginning_date, '%Y-%m-%d %H:%M:%S')
        print(datetime.datetime.now() - beginning_date)
        delta_day = (datetime.datetime.now() - beginning_date).days
        '''
    elif time==constants.time['1y']:
        df = df.iloc[:360, :]
    elif time==constants.time['5y']:
        df = df.iloc[:1800, :]
    else:
        df = df
    df.index = pd.to_datetime(df.index)
    df = df[::-1]
    return df

def process_data(df):
    first_entry = df.iloc[:1, :]
    print("first in df: ", df.iloc[:1, :])
    open_price = first_entry.iloc[0][0]
    close = first_entry.iloc[0][1]
    low = first_entry.iloc[0][2]
    high = first_entry.iloc[0][3]
    volume = first_entry.iloc[0][4]
    print("open: {}\nclose: {}\n low: {}\n high: {}\nvolumn:{}".format(open_price, close, low, high, volume))
    return {'open': open_price, 'close': close, 'low': low, 'high': high, 'volume':volume}

def get_processed_data(time, tick):
    df = read_json()
    # df = get_data(time, tick)
    ret_df = splice_data(df, time)
    meta_data = process_data(ret_df) 
    ret_df = (ret_df['4. close'])
    return [ret_df, meta_data]

if __name__ == '__main__':
    (get_processed_data(constants.time['ytd'], 'NFLX'))
    # print(get_data(constants.time['1d'], 'NFLX'))
