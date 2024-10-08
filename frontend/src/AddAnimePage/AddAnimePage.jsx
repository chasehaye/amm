import React from "react";
import NewAnimeForm from "../Components/NewAnimeForm/NewAnimeForm"
function AddAnimePage() {

    return(
        <>
            <h1 class="text-yellow-500">Add Anime Page</h1>
            <h3>adjsut model fields, secure for admin</h3>
            <h3>create api call</h3>
            <h3>consider making a seperate component to indvidualy display current info</h3>


            <NewAnimeForm />
        </>
    )
}

export default AddAnimePage;