import React, { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createNewAnime } from "../../utilities/anime-api"; 

const NewAnimeForm = () => {
    const navigate = useNavigate();
    const [ error, setError ] = useState('');

    // Anime fields
    const titleEnglishRef = useRef('');
    const titleJpRomanRef = useRef('');
    const titleJpKanjiRef = useRef('');
    const descriptionRef = useRef('');

    async function handleSubmit(e) {
        e.preventDefault();
        setError('');
        const newAnime = {
            titleEnglish: titleEnglishRef.current.value,
            titleJpRoman: titleJpRomanRef.current.value,
            titleJpKanji: titleJpKanjiRef.current.value,
            description: descriptionRef.current.value
        }
        try{
            const newAnimeCallResponse = await createNewAnime(newAnime);
            console.log("consider redirect for create page this call comes from new anime form")
        }catch{
            setError(error)
        }
    }



    return(
        <>
        <h1>Add naime form</h1>
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="eng">English</label>
                <input type="text" id="eng" ref={titleEnglishRef} className="border border-black px-2 py-1"/>
            </div>
            <div>
                <label htmlFor="">Romanized Jp</label>
                <input type="text" ref={titleJpRomanRef} className="border border-black px-2 py-1"/>
            </div>
            <div>
                <label htmlFor="">Kanji Jp</label>
                <input type="text" ref={titleJpKanjiRef}className="border border-black px-2 py-1"/>
            </div>
            <div>
                <label htmlFor="">Description</label>
                <input type="text" ref={descriptionRef}className="border border-black px-2 py-1"/>
            </div>

            <div className="mx-auto">
                <button className="bg-red-500 text-black py-1 px-6 rounded text-sm hover:bg-C8 mt-2 h-10 font-bold">Add</button>
            </div>

        </form>
        </>
    )
}

export default NewAnimeForm;