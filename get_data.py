from alpha_vantage.timeseries import TimeSeries
import constants
import datetime

def get_data(time, tick):

    ts = TimeSeries(key='VVKDMK4DCJUF1NQP', output_format='pandas')
    if time == constants.time['1d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='5min', outputsize='compact')
    elif time == constants.time['5d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='30min', outputsize='compact')
    elif time == constants.time['1m']:
        data,meta_data = ts.get_daily(symbol=tick, outputsize='compact')
    else:
        data, meta_data = ts.get_daily(symbol=tick, outputsize='full')
    data = data[::-1]
    most_recent_date = datetime.datetime.strptime(data.iloc[0].name, '%Y-%m-%d %H:%M:%S')
    current_date = datetime.datetime.now()

    print(most_recent_date)
    print(current_date)
    print("comparison: ", most_recent_date < current_date)
    return data,meta_data

if __name__ == '__main__':
    (get_data(constants.time['1d'], 'NFLX'))
