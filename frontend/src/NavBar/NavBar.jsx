import React, { useContext } from "react";
import { UserContext } from '../UserProvider';
import './NavBar.css';

function NavBar() {
    const { user } = useContext(UserContext);

    return(
        <>
            <div className="bg-slate-700 mt-4 flex w-full nav_w">
                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    <p>Home</p>
                </div>

                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    <p>Trending</p>
                </div>

                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    <p>manga</p>
                </div>
                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    <p>anime</p>
                </div>
                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    <p>Search</p>
                </div>
                <div className="p-2 border border-gray-400 flex-1 text-center cursor-pointer hover:bg-slate-600">
                    {user ? user.name : 'No user logged in'}
                </div>
            </div>
        </>
    )
}

export default NavBar