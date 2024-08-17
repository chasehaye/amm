import React, { useContext, useEffect, useState } from 'react';
import { index } from '../utilities/anime-api';

function AnimeList() {

    const [animeList, setAnimeList] = useState([]);

    useEffect(() => {
        async function fetchAnime() {
            try {
                const data = await index();
                setAnimeList(data);
            } catch (err) {
                console.error("Failed to fetch Anime List", error);
            }
        }

        fetchAnime();
    }, []);

    return(
        <>
            <div className="w-[80vw] h-screen justify-center items-center bg-gray-900 mx-auto">
                <div className="text-center top-0 text-red-500">
                    Test block
                </div>








            <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {animeList.length > 0 ? (
                    animeList.map((anime) => (
                        <div key={anime.id} className="bg-gray-800 p-4 rounded-lg shadow-md">
                            <h3 className="text-white text-lg mb-2">{anime.titleEnglish}</h3>
                            <p>{anime.id}</p>
                        </div>
                    ))
                ) : (
                    <p className="text-white">Loading...</p>
                )}
            </div>















                
            </div>
        </>
    )
}

export default AnimeList