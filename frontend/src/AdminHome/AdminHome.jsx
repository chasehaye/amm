import React, { useState } from "react";
import AdminNav from "../Components/AdminNav/AdminNav";

function AdminHomePage() {
    const [loading, setLoading] = useState(true)

    return(
        <>
            <AdminNav />
            <h1>Admin home page</h1>
        </>
    )

}

export default AdminHomePage;