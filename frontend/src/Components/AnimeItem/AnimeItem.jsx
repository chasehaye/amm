import React from "react";
import { Link } from "react-router-dom";

function AnimeItem({anime}) {

    return(
        <>
        <div className="flex space-x-4 p-4 w-[80vw] mx-auto border">
            <Link to={`/anime/${anime.id}`}>
            <div className="flex-1">
                {anime.id}
            </div>
            </Link>

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

export default AnimeItem;