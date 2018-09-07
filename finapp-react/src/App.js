import React, { Component } from 'react';
import './App.css';
// import * as Highcharts from 'highcharts'
import HighChart from './HighChart/HighChart'
import ArticleList from './ArticleList/ArticleList'

class App extends Component {
  state = {
    data: [],
    options: {
      rangeSelector: {
        selected: 1
      },
      title: {
        text: 'stock price',
      },
      series: [{
        name: 'stock price',
        data: [1, 2, 3],
        type: 'spline',
        tooltip: {
          valueDecimals: 2
        }
      }]
    }
  }

  render() {
    return (
      <div>
        <div className='App-header'>
        </div>
        <div className="body">
          <div className="column column-graph">
            <HighChart options={this.state.options} />
          </div>
          <div className="column column-article">
            <ArticleList/>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
