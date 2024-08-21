import React, { useContext, useEffect, useState } from "react";
import { adminVerify } from "../../utilities/user-service";
import { Link } from "react-router-dom";

function AdminNav() {
    const [admin, setAdmin] = useState(null);

    useEffect(() => {
        const fetchAdminStatus = async () => {
            try {
                const adminStatus = await adminVerify();
                setAdmin(adminStatus)
            } catch (err) {
                setAdmin(false)
            } 
        }
        fetchAdminStatus();
    }, [])

    


    if (admin === false){
        return null;
    }
    return(
    <>
    <div className="fixed bottom-0 w-full flex">
        <Link className="cursor-pointer flex-1 text-center bg-black text-white" to="/admin/anime/add">Add Anime</Link>
        <div className="cursor-pointer flex-1 text-center bg-black text-white">2</div>
        <div className="cursor-pointer flex-1 text-center bg-black text-white">3</div>
        <div className="cursor-pointer flex-1 text-center bg-black text-white">4</div>
        <div className="cursor-pointer flex-1 text-center bg-black text-white">
            Admin Status: {admin !== null ? admin.toString() : "Loading..."}
        </div>
    </div>
    </>
    )
}

export default AdminNav;