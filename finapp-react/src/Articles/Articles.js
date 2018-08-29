import React, { Component } from 'react';
import axios from 'axios';


class Articles extends Component {

    state = {
        data: []
    }

    constructor(props) {
        super(props);
        this.chartContainer = React.createRef();
    }

    componentDidMount() {
        var today = new Date()
        let day = today.getDate()
        let month = today.getMonth() + 1;
        let year = today.getFullYear();
        console.log(today)
        console.log(today.getDate())
        console.log(today.getUTCMonth())
        console.log(today.getFullYear())
        axios.get(`http://127.0.0.1:5000/Scrape?ticker=msft&mm=${month}&yy=${year}&dd=${day}`)
            .then(response => {
                console.log(response.data);
                return response.data;
            })    
    }

    render() {
        return (
            <div>
                Articles
            </div>
        );
    }
}

export default Articles;
