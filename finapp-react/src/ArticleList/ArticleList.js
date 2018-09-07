import React, { Component } from 'react';
import axios from 'axios';
import FinArticle from './Article/Article';
import './ArticleList.css';

class ArticleList extends Component {

    state = {
        data: []
    };

    constructor(props) {
        super(props);
        this.chartContainer = React.createRef();
    }

    componentDidMount() {
        var today = new Date()
        let day = today.getDate()
        let month = today.getMonth() + 1;
        let year = today.getFullYear();
        var counter = 0;
        axios.get(`http://127.0.0.1:5000/Scrape?ticker=msft&mm=${month}&yy=${year}&dd=${day}`)
            .then(response => {
                this.setState({data: response.data.articleList});
                counter = counter + 1;
            });
    }

    render() {
        /*
        const posts = this.state.data.map(post => {
            return <Article key={post.time} date={post.time}/>
        });
        */
        const posts = this.state.data.map(article => {
            return <FinArticle 
            key={article.time} 
            date={article.time}
            title={article.article_bio} 
            link={article.article_link}
            author={article.author}
            />;
        })
        return (
            <div>
                <div className='articleBox'>
                    {posts}
                </div>
            </div>
        );
    }
}

export default ArticleList;
