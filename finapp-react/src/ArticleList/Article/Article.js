import React from 'react';
import './Article.css'


const finArticle = (props) => {
    return (
        <div className='post'>
            <a href={props.link}>
                <h1>{props.title} </h1>
                <div>
                    by {props.author}
                </div>
                <div>
                    {props.date}
                </div>
            </a>
        </div>
    )
}

export default finArticle;
