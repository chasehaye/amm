import React from "react";

function Anime({anime}) {

    return(
        <>
        <div className="flex space-x-4 p-4 w-[80vw] mx-auto border">
            <div className="flex-1">
                {anime.id}
            </div>

            <div className="flex-1">
                {anime.titleEnglish}
            </div>

            <div className="flex-1">
                genre
            </div>
                
            <div className="flex-1">
                air start
            </div>
                
            <div className="flex-1">
                air end
            </div>

            <div className="flex-1">
                rating
            </div>

        </div>
        </>
    )
}

export default Anime;