import React, { useContext, useEffect, useState } from 'react';
import { index } from '../../utilities/anime-api';
import Anime from '../../Components/AnimeItem/AnimeItem';

function AnimeList() {

    const [animeList, setAnimeList] = useState([]);

    useEffect(() => {
        async function fetchAnime() {
            try {
                const anime = await index();
                const mappedAnime = anime.map(anime => (
                    <Anime key={anime.id} anime={anime} />
                ))
                setAnimeList(mappedAnime);
            } catch (err) {
                console.error("Failed to fetch Anime List", err);
            }
        }

        fetchAnime();
    }, []);

    return(
        <>
            <div className="pt-10 h-screen justify-center items-center mx-auto bg-gray-400">
                
                
                {animeList}

                
            </div>
        </>
    )
}

export default AnimeList;