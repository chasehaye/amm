import React, { useContext } from 'react';
import { UserContext } from '../UserProvider';

function Home() {

    const { user, setUser } = useContext(UserContext);

    return (
        <>
            <h1>Home Page</h1>
            <div>
                <p>User: {user ? user.name : 'No user logged in'}</p>
            </div>
        </>
    );
}

export default Home