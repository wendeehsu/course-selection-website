import React from 'react';
import Icon from './icon';
import '../../style/search.css';

const SearchBar = ({title, placeholder}) => {
    return (
        <div className='search-section'>
            <h2>{title}</h2>
            <form role="search">
                <input id="search" type="search" placeholder={placeholder} />
                <button type="submit"><Icon.Search/></button>    
            </form>
        </div>
    )
}

export default SearchBar;