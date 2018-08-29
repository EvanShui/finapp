import React, { Component } from 'react';
import axios from 'axios';

class Graph extends Component {
componentDidMount () {
    axios.get('http://127.0.0.1:5000/Data?ticker=msft&time=ytd').then(response => {
        console.log(response);
    });
}
  render() {
    return (
        <div>
            <p>hello</p>
        </div>
    );
  }
}

export default Graph;
