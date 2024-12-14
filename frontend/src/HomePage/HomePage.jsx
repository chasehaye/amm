import React, { useContext } from 'react';
import { UserContext } from '../UserProvider';
import NavBar from '../Components/NavBar/NavBar';

function Home() {

    const { user } = useContext(UserContext);

    return (
        <>
            <NavBar/>
            <div className="flex justify-center items-center w-full">
                landing - {user.name}
            </div>
        </>
    );
}

export default Home