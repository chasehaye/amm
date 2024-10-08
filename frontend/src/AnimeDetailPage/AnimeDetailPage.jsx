import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getAnimeRequest } from "../utilities/anime-api";
import AnimeItemDetail from "../Components/AnimeItemDetail/AnimeItemDetail";

function AnimeItemPage() {
    let { animeId } = useParams();
    const [ anime, setAnime ] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchAnime(){
            try{
                const animeData = await getAnimeRequest(animeId);
                if(animeData){
                    setAnime(animeData);
                    setLoading(false);
                }else{
                    setError("Not found");
                    setLoading(false);
                }
            }catch(error) {
                setError("Error retreving");
                setLoading(false);
            }
        }
        if(animeId){
            fetchAnime();
        }
    }, [animeId]);

    return (
        <>
            {loading ? 
                <p>Loading</p>
            :
            error ? 
                <p>{error}</p>
            :
            <AnimeItemDetail anime={anime} setAnime={setAnime}/>
            }
        </>
    )
}

export default AnimeItemPage;