from alpha_vantage.timeseries import TimeSeries
import constants

def get_data(time, tick):

    ts = TimeSeries(key='VVKDMK4DCJUF1NQP', output_format='pandas')
    if time == constants.time['1d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='5min', outputsize='compact')
    elif time == constants.time['5d']:
        data,meta_data = ts.get_intraday(symbol=tick, interval='30min', outputsize='compact')
    elif time == constants.time['1m']:
        data,meta_data = ts.get_daily(symbol=tick, outputsize='compact')
    else:
        data, meta_data = ts.get_daily(symbol=stock_ticker, outputsize='full')
    return data,meta_data

if __name__ == '__main__':
    print(get_data(constants.time['1d'], 'NFLX'))
