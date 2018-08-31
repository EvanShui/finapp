# pandas
import pandas as pd

# flask files
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

# local files
from scraper import web_scraper
from get_data import get_processed_data
import json
import constants

app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://localhost:3000", allow_headers=['Access-Control-Allow-Credentials', 'Authorization', 'Content-type'])
parser = reqparse.RequestParser()
parser.add_argument('ticker', type=str)
parser.add_argument('dd', type=int)
parser.add_argument('mm', type=int)
parser.add_argument('yy', type=int)
parser.add_argument('time', type=str)
todos = {1: 'hello'}

class RetTicker(Resource):
    def get_data(self, arg):
        return('base_url' + arg)

    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        func = self.get_data(ticker)
        return {ticker: '{}'.format(func)}

class ScrapeTick(Resource):
    def scrape(self, ticker, day, month, year):
        articles = web_scraper(ticker, day, month, year)
        return (articles)

    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        day = args['dd']
        month = args['mm']
        year = args['yy']
        articles = self.scrape(ticker, day, month, year)
        if articles:
            return {
                'status': 'OK',
                'articleList': articles
                }
        else:
            return {
                'status': 'Error',
                'msg': 'unable to retrieve list'
            }

class DataTick(Resource):
    def get_data(self, ticker, time):
        print(ticker, time)
        data = get_processed_data(time, ticker)
        print("-------------")
        data[0].index = (pd.to_datetime(data[0].index))
        print("-------------")
        return data
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        time = args['time']
        graph_data = self.get_data(ticker, constants.time[time])
        graph_data[0] = graph_data[0].to_json()
        if graph_data: 
            return {
                'status': 'Ok',
                'data': graph_data[0],
                'meta_data': graph_data[1]
            }
        else:
            return {
                'status': 'Error',
                'msg': 'unableto retrieve data'
            }

class BioTick(Resource):
    def get_bio(self, arg):
        return('biography for {}'.format(arg))
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        bio = self.get_bio(ticker)
        return {'biography': bio}

api.add_resource(RetTicker, '/Ticker')
api.add_resource(ScrapeTick, '/Scrape')
api.add_resource(DataTick, '/Data')
api.add_resource(BioTick, '/Bio')

if __name__ == '__main__':
    app.run(debug=True)