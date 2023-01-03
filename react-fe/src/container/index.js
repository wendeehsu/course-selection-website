import React, { useState, useEffect } from 'react';
import SearchBar from '../component/ui/searchBar';
import '../style/page/home.css';

function Index() {
    return (
        <>
            <div className='top-section'>
                <SearchBar
                    title="Look for a course"
                    placeholder="e.g. Information Architecture"/>
            </div>
        </>
    )
}

export default Index;