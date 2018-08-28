# flask files
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

# local files
from scraper import web_scraper
from get_data import get_processed_data

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('dd', type=int)
parser.add_argument('ticker', type=str)
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
                'article list': articles
                }
        else:
            return {
                'status': 'Error',
                'msg': 'unable to retrieve list'
            }

class DataTick(Resource):
    def get_data(self, ticker, time):
        data = get_processed_data(ticker, time)
        return data
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        time = args['time']
        graph_data = self.get_data(ticker, time)
        return {'graph data': graph_data}

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