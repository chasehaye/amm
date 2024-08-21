import React, { useContext, useState, useEffect } from "react";
import { UserContext } from '../../UserProvider';
import './NavBar.css';
import { Link } from "react-router-dom";
import { adminVerify } from "../../utilities/user-api";

function NavBar() {
    const { user } = useContext(UserContext);
    const [admin, setAdmin] = useState(null);

    useEffect(() => {
        const fecthAdminStatus = async () => {
            try {
                const adminStatus = await adminVerify();
                setAdmin(adminStatus)
            } catch (err) {
                console.log(err)
                setAdmin(false)
            } 
        }
        fecthAdminStatus();
    }, [])

    return (
        <>
            {admin === null ? (
                null
            ) : admin ? (
                <div>
                    <div className="font-bold border border-black inline-block m-4">
                        Admin
                    </div>
                    <Link className="font-bold border border-black inline-block m-4" to="/admin/home">
                        Menu
                    </Link>
                </div>
            ) : (
                <div className="font-bold border border-black inline-block m-4">
                    AMM
                </div>
            )}

            <div className="mt-10 flex w-full nav_w">
                <Link className="p-2 text-center flex-1 cursor-pointer hover:font-bold relative" to="/a">
                    <p>Home</p>
                    <span className="absolute bottom-1/2 transform translate-y-1/2 right-0 h-20 border-r-2 border-black"></span>
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </Link>

                <div className="p-2 flex-1 text-center cursor-pointer hover:font-bold relative">
                    <p>Trending</p>
                    <span className="absolute bottom-0 transform translate-y-1/2 right-0 h-20 border-r-2 border-black"></span>
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </div>

                <div className="p-2 flex-1 text-center cursor-pointer hover:font-bold relative">
                    <p>manga</p>
                    <span className="absolute bottom-1/2 transform translate-y-1/2 right-0 h-20 border-r-2 border-black"></span>
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </div>
                <div className="p-2 flex-1 text-center cursor-pointer hover:font-bold relative">
                    <p>anime</p>
                    <span className="absolute bottom-0 transform translate-y-1/2 right-0 h-20 border-r-2 border-black"></span>
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </div>
                <div className="p-2 flex-1 text-center cursor-pointer hover:font-bold relative">
                    <p>Search</p>
                    <span className="absolute bottom-1/2 transform translate-y-1/2 right-0 h-20 border-r-2 border-black"></span>
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </div>
                <div className="p-2 flex-1 text-center cursor-pointer hover:font-bold relative">
                    {
                    user 
                    ? 
                    user.name 
                    :             
                    <Link to='/auth'>
                        <button>
                            Login
                        </button>
                    </Link>
                    }
                    <span className="absolute right-0 bottom-0 w-full h-1/2 border-b-2 border-black"></span>
                </div>
            </div>

            <div className="flex w-full nav_w mb-20">
                    <div className="p-2 flex-1 text-center cursor-pointer relative"></div>
                    <div className="p-2 flex-1 text-center cursor-pointer relative">modal</div>
                    <div className="p-2 flex-1 text-center cursor-pointer relative">modal</div>
                    <div className="p-2 flex-1 text-center cursor-pointer relative">modal</div>
                    <div className="p-2 flex-1 text-center cursor-pointer relative"></div>
                    <div className="p-2 flex-1 text-center cursor-pointer relative"></div>
            </div>
        </>
    )
}

export default NavBar;