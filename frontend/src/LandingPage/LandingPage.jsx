import React from 'react';
import AnimeList from './AnimeList/AnimeLIst';
import NavBar from '../NavBar/NavBar';
import { Link } from 'react-router-dom';

function LandingPage() {
    return (
        <>
            <p>LandingPage</p>
            <Link to='/auth'>
                <button>
                    Login/SignUp
                </button>
            </Link>
            <NavBar />
            <AnimeList />
        </>
    )

}

export default LandingPage;