import React, { Component } from 'react';
import Highcharts from 'highcharts/highstock'
import axios from 'axios';


class HighChart extends Component {

    state = {
        data: []
    }

    constructor(props) {
        super(props);
        this.chartContainer = React.createRef();
    }

    componentDidMount() {
        this.chart = new Highcharts.chart(
            this.chartContainer.current,
            this.props.options
        );

        const temp_lst = []
        axios.get('http://127.0.0.1:5000/Data?ticker=msft&time=ytd')
            .then(response => {
                return response.data;
            }).then(data => {
                var json_data = JSON.parse(data.data);
                for (var key in JSON.parse(data.data)) {
                    var date = new Date(parseInt(key, 10) + 28800000);
                    temp_lst.push([
                        date,
                        json_data[key]
                    ]);
                };
                return temp_lst;
            }).then( data =>{
                this.chart.series[0].setData(data);
            });
    }

    render() {
        return (
            <div ref={this.chartContainer} />
        );
    }
}

export default HighChart;
