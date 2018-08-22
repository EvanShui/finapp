from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('ticker', type=str)
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
    def scrape(self, arg):
        return('scraping for {}'.format(arg))
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        articles = self.scrape(ticker)
        return {'article list': articles}

class GraphTick(Resource):
    def get_graph(self, arg):
        return('graph data for {}'.format(arg))
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        graph_data = self.get_graph(ticker)
        return {'graph data': graph_data}

class StatsTick(Resource):
    def get_stats(self, arg):
        return('statistics for {}'.format(arg))
    
    def get(self):
        args = parser.parse_args()
        ticker = args['ticker']
        stats = self.get_stats(ticker)
        return {'statistic': stats}

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
api.add_resource(GraphTick, '/Graph')
api.add_resource(StatsTick, '/Stats')
api.add_resource(BioTick, '/Bio')


if __name__ == '__main__':
    app.run(debug=True)