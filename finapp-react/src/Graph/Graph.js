import React, { Component } from 'react';
import axios from 'axios';

class Graph extends Component {
    state = {
        data: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/Data?ticker=msft&time=ytd').then(response => {
            console.log(response.data)
            this.setState({data: response.data})
            console.log(this.state.data)
        });
    }
    render() {
        const data = this.state.data.map(data=> {
            return <div>{data}</div>
        })
        return (
            <div>
                {data}
                <p>hello</p>
            </div>
        );
    }
}

export default Graph;
