import React from "react";
import { Link } from "react-router-dom";

function AnimeItem({anime}) {

    return(
        <>
        <div className="justify-center items-center mx-auto">
            <div className="flex p-5 w-[70vw] mx-auto border border-c4">
                <div className="w-[30vw] justify-center text-center">
                <Link to={`/anime/${anime.id}`}>
                    <div className="flex flex-row">
                        {
                        anime.image ? (
                            <img 
                            src={anime.image} 
                            alt={"?"} 
                            className="w-[87px] h-[123px] object-cover ml-[1vw]" 
                            />
                        ) : (
                            <div className="w-[87px] h-[123px] my-4 mx-4 bg-c4 text-c6 flex items-center justify-center"><span className="text-5xl">?</span></div>
                        )
                        }
                        <div className="flex-1 px-[8vw] text-left">
                            {anime.titleEnglish ? anime.titleEnglish : anime.titleJpRoman}
                        </div>
                    </div>
                </Link>
                </div>


                <div className="w-[10vw] justify-center text-center">
                    {anime.episodes ? anime.episodes : "N/A"}
                </div>
                    
                <div className="w-[10vw] justify-center text-center">
                    {anime.premiereSeason ? anime.premiereSeason : "N/A"}
                </div>
                    
                <div className="w-[10vw] justify-center text-center">
                    <span>
                        {anime.studio?.name ? anime.studio.name : "N/A"}
                    </span>
                </div>

                <div className="w-[10vw] justify-center text-center">
                    {anime.aggregateRating ? anime.aggregateRating : "N/A"}
                </div>


            </div>
        </div>
        </>
    )
}

export default AnimeItem;