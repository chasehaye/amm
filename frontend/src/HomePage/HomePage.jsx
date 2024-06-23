import React, { useContext } from 'react';
import { UserContext } from '../UserProvider';

function Home() {

    const { user } = useContext(UserContext);

    return (
        <>
            <h1>Home Page</h1>
            <div>
                <p>The user is globally accesible below:</p>
                <p> {user ? user.name : 'No user logged in'}</p>
            </div>
        </>
    );
}

export default Home