import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getAnimeRequest, deleteAnimeRequest } from "../utilities/anime-api";
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

    async function handleDelete(e){
        try{
            const deleteResponse = await deleteAnimeRequest(anime.id);
            if(deleteResponse.message === 'success'){
                navigate('/')
            }
        }catch(error){
            console.log(error);
        }
    }

    return (
        <>
            {loading ? 
                <p>Loading</p>
            :
            error ? 
                <p>{error}</p>
            :
            <div>
                <AnimeItemDetail anime={anime} setAnime={setAnime}/>
                <div className="mx-auto" onClick={handleDelete}>
                    <button className="bg-red-500 text-black py-1 px-6 rounded text-sm hover:bg-C8 mt-2 h-10 font-bold">delete</button>
                </div>
                <div>
                    ADD UPDATE PAGE
                </div>
            </div>
            }
        </>
    )
}

export default AnimeItemPage;