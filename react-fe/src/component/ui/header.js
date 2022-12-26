import React from 'react';
import { Link } from 'react-router-dom';
import '../../style/header.css';

const Header = () => {
    return (
        <>
            <nav className="navMenu">
                <Link to="#">Home</Link>
                <Link to="#">Courses</Link>
                <Link to="#">Instructors</Link>
                <Link to="#">Resource</Link>
                <div className="dot"></div>
            </nav>
        </>
    )
}

export default Header;