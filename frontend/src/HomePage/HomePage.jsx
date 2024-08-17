import React, { useContext } from 'react';
import { UserContext } from '../UserProvider';
import NavBar from '../NavBar/NavBar';
import TestEnv from '../TestEnv/TestEnv';

function Home() {

    const { user } = useContext(UserContext);

    return (
        <>
            <NavBar/>
            <div className='justify-center text-center'>Home Page</div>
            <div className='justify-center text-center'>
                Start writing backend logic for api calls
            </div>
            <div className='justify-center text-center'>
                Start writing api calls to get user filtered anime list
            </div>
            <TestEnv/>
        </>
    );
}

export default Home