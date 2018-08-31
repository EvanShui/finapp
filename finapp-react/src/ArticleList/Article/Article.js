import React from 'react';
import './Article.css'


const finArticle = (props) => {
    return (
        <div class='post'>
            <a href={props.link}>
                <h1>{props.title} by {props.author}</h1>
                <div>
                    {props.date}
                </div>
            </a>
        </div>
    )
}

export default finArticle;
