import React, { useContext, useEffect, useState } from "react";
import { UserContext } from '../../UserProvider';
import { adminVerify } from "../../utilities/user-service";

function AdminNav() {
    const [admin, setAdmin] = useState(null);

    useEffect(() => {
        const fecthAdminStatus = async () => {
            try {
                const adminStatus = await adminVerify();
                setAdmin(adminStatus)
            } catch (err) {
                setAdmin(false)
            } 
        }
        fecthAdminStatus();
    }, [])

    


    if (admin === false){
        return null;
    }
    return(
    <>
    <div className="fixed bottom-0 w-full flex">
        <div className="flex-1 text-center bg-black text-white">1</div>
        <div className="flex-1 text-center bg-black text-white">2</div>
        <div className="flex-1 text-center bg-black text-white">3</div>
        <div className="flex-1 text-center bg-black text-white">4</div>
        <div className="flex-1 text-center bg-black text-white">
            Admin Status: {admin !== null ? admin.toString() : "Loading..."}
        </div>
    </div>
    </>
    )
}

export default AdminNav;