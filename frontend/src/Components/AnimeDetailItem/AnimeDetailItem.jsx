import React, { useContext, useEffect, useState } from "react";
import { getAbbrvAnimeRequest } from "../../utilities/anime-api";
import { linkAnimeToUser, retrieveUserRating, updateUserAnimeRating } from "../../utilities/user-api";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../../UserProvider";

function AnimeDetailItem ({anime}) {

    const { user } = useContext(UserContext);
    const [animePrequel, setAnimePrequel] = useState(null);
    const [animeSequel, setAnimeSequel] = useState(null);
    const [loadingPrequel, setLoadingPrequel] = useState(true);
    const [loadingSequel, setLoadingSequel] = useState(true); 
    const navigate = useNavigate();

    const redirectToPrev = () => {
        navigate(-1);
    };

    const redirectToHome = () => {
        navigate('/');
    }

    useEffect(() => {
        async function fetchPreAndSeq() {
            try {
                if(anime.prequel){
                    const prequel = await getAbbrvAnimeRequest(anime.prequel);

                    setAnimePrequel(prequel);
                }else{
                    setAnimePrequel(null);
                }
                if(anime.sequel){
                    const sequel = await getAbbrvAnimeRequest(anime.sequel);

                    setAnimeSequel(sequel);
                }else{
                    setAnimeSequel(null);
                }
            }catch(err){
                console.log(err);
            }finally {
                setLoadingPrequel(false);
                setLoadingSequel(false);
            }
        }
        if (anime) {
            fetchPreAndSeq();
        }
    }, [anime]);

    // handle adding of anime to user lists
    const [isSelectVisible, setIsSelectVisible] = useState(false);
    // Toggle dropdown visibility
    const toggleLinkingMenu = () => {
        setIsSelectVisible(!isSelectVisible);
    };
    const [isValidLinkEstablished, setIsValidLinkEstablished] = useState(null);

    const handleSelectionLinkage = async (selection) => {
        const queryParameters = {
            user_id: user.id,
            anime_id: anime.id,
            list_type: selection,
        };
        const linkResponse = await linkAnimeToUser(user.name, queryParameters);
        if(linkResponse.message === "success"){
            setIsValidLinkEstablished(selection)
        }
        setIsSelectVisible(false);
    }

    useEffect(() => {
        if (isValidLinkEstablished !== null) {
          const timer = setTimeout(() => {
            setIsValidLinkEstablished(null);
          }, 3000);
          return () => clearTimeout(timer);
        }
    }, [isValidLinkEstablished]);

    // opening close rating menu
    const [isRatingMenuHovered, setIsRatingMenuHovered] = useState(false);
    const [userRating, setUserRating] = useState("-")

    useEffect(() => {
        async function fecthAnimeRatingFromUser() {
            try{
                const response = await retrieveUserRating(user.name, anime.id, {userId: user.id});
                setUserRating(response.rating)
            }catch(e){
                console.log(e)
            }
        }

        fecthAnimeRatingFromUser();
    }, []);

    const handleRatingUpdate = async (selection) => {
        try{
            const queryParameters = {
                userId: user.id,
                score: selection,
            };
            const response = await updateUserAnimeRating(user.name, anime.id, queryParameters);
            setUserRating(response.rating);
            setIsRatingMenuHovered(false);
        }catch(err){
            console.log(err)
        }
    }


    return (
        <>
        <div className="flex justify-between mt-2">
            <div className="border-b border-c4 w-[55%] pl-10">
                {anime.titleEnglish ? (
                    <>
                        <div className="text-2xl font-semibold">{anime.titleEnglish}</div>
                        {anime.titleJpRoman && (
                            <div className="text-lg mt-1 mb-2">{anime.titleJpRoman}</div>
                        )}
                    </>
                ) : (
                    anime.titleJpRoman && (
                        <div className="text-xl font-semibold mb-2">{anime.titleJpRoman}</div>
                    )
                )}
                
            </div>

            <button className="hover:bg-c2 hover:text-c6 border-t border-r border-c4 p-2 h-[50%] mt-4 hover:text-c2 hover:border-c2 w-20" onClick={redirectToHome}><span>Home</span></button>
            <button className="hover:bg-c2 hover:text-c6 border-l border-b border-c4 p-2 h-[50%] mt-4 hover:text-c2  hover:border-c2 w-20" onClick={redirectToPrev}><span>Back</span></button>

            <div className="self-end border-b border-c4 w-[25%]">
                {anime.titleJpKanji && (
                    <div className="text-md mb-2 text-right mr-10">{anime.titleJpKanji}</div>
                )}
            </div>

        </div>

        <div className="flex">

            <div className="w-[25%] border-r  border-c4 h-[40vw]">
                {anime.image ? (
                    <img 
                        src={anime.image} 
                        alt="Image" 
                        className="w-[406px] h-[574px] mx-auto mt-4" 
                    />
                ) : (
                    <div className="w-[406px] h-[574px] my-4 mx-4 bg-c4 text-c6 flex items-center justify-center"><span className="text-[200px]">?</span></div>
                )}
                <div className="border-t border-c4 mt-4">




                    <div className="border-b border-c4 flex">
                        <div className="mx-auto cursor-pointer border-r border-l border-c4 my-2 px-2 hover:text-c2" onClick={toggleLinkingMenu}>
                            {isSelectVisible ? <div>Close</div> : <div>Add Anime</div>}
                        </div>
                    </div>

                    {isSelectVisible && (
                        <div className="mt-2 pt-2 px-1 ml-14">
                            <ul>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(1)}>Add to currently watching</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(2)}>Add to completed</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(3)}>Add to plan to watch</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(4)}>Add to dropped</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(5)}>Add to interested in</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                                <li className="py-1 hover:text-c2 cursor-pointer" onClick={() => handleSelectionLinkage(6)}>Add to on hold</li>
                                <div className="border-b border-c4 w-[50%] ml-2"></div>
                            </ul>
                        </div>
                    )}
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 1 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to currently watching</p>
                    </div>
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 2 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to completed</p>
                    </div>
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 3 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to plan to watch</p>
                    </div>
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 4 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to dropped</p>
                    </div>
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 5 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to interested in</p>
                    </div>
                    <div className={`flex items-center justify-center mt-2 ${isValidLinkEstablished !== 6 ? 'hidden' : ''}`}>
                    <p className="text-c2">Added to on hold</p>
                    </div>



                    <div className="mx-auto text-center mt-2 mb-1">Information</div>

                    <div className="border-t border-c4 w-3/4"></div>
                    <div className="flex mt-2">
                        <div className="ml-2 mr-2">{`Episodes: ${anime.episodes}` || "?"}</div>
                        <span className="">|</span>
                        <div className="ml-2">{anime.episodeDuration ? `Duration: ${anime.episodeDuration} min. per` : "?"}</div>
                    </div>


                    <div className="flex mt-2">
                        <div className="ml-2">Aired: </div>
                        <div className="ml-2">
                            {anime.airDate
                                ? (() => {
                                    const [year, month, day] = anime.airDate.split('-');
                                    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
                                    return `${months[parseInt(month, 10) - 1]} ${parseInt(day, 10)}, ${year}`;
                                })()
                                : "?"}
                        </div>
                        <span className="ml-2">-</span>
                        <div className="ml-2">
                            {anime.endDate
                                ? (() => {
                                    const [year, month, day] = anime.endDate.split('-');
                                    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
                                    return `${months[parseInt(month, 10) - 1]} ${parseInt(day, 10)}, ${year}`;
                                })()
                                : "?"}
                        </div>
                    </div>

                    <div className="mt-2 w-[75%]">
                        {anime.genre ? (
                            <>
                            <div className="ml-2">
                            <span>Genre: </span>
                                {anime.genre && anime.genre.length > 0
                                ? anime.genre.map((genre, index) => (
                                    <span key={index}>
                                        {genre}
                                        {index < anime.genre.length - 1 && ", "}
                                    </span>
                                ))
                                : "No genres available"}
                            </div>
                            </>
                        ) : (
                            <div className="ml-2">Genre (Not Available)</div>
                        )}
                    </div>

                    <div className="ml-2 mt-2">
                    {anime.demographic ? (
                            <div className="">Demographic: {anime.demographic}</div>
                        ) : (
                            <div className="">Demographic (Not Available)</div>
                        )}
                    </div>

                    <div className="mt-2 ml-2">
                        Type: {anime.type}
                    </div>




                </div>  
                
            </div>


            <div className="w-[75%] flex flex-col">

                <div className="flex border border-c4 rounded-lg ml-[10%] mt-4 w-[40%]">
                    <div className="m-3">
                        <div className="text-center">Rating</div>
                        <div className="text-3xl">{anime.aggregateRating || "N/A"}</div>
                    </div>
                    <div className="mt-3">
                        <div>{anime.premiereSeason || "No premiere season"}</div>
                        <div className="flex">
                            <div className="mr-3">{anime.type || "No type specified"}</div>
                            <span>|</span>
                            <div className="mr-3 ml-3">{anime.studio?.name || "No studio"}</div>
                        </div>
                    </div>
                </div>
                
                <div className="flex w-[50%] mx-auto mt-4 border border-c4 rounded-md relative">
                    <div className="flex border-b border-r border-c4 m-2 w-[20%] py-1 pl-2 group cursor-pointer" onMouseEnter={() => setIsRatingMenuHovered(true)}  onMouseLeave={() => setIsRatingMenuHovered(false)}>
                        <div className="flex">
                            <div className="">
                                rating
                            </div>
                            <div className="pl-1 text-c2 hover:text-c4 group-hover:text-c4">
                                v
                            </div>
                        </div>
                        <div className="mx-auto">
                           {userRating}
                        </div>
                    </div>
                    {isRatingMenuHovered && (
                        <div className="absolute mt-10 mx-2 left-0 w-[20%] border-x border-t border-c4 bg-c6 z-10 text-center flex flex-col" onMouseEnter={() => setIsRatingMenuHovered(true)}  onMouseLeave={() => setIsRatingMenuHovered(false)}>
                        {Array.from({ length: 10 }, (_, index) => (
                            <div key={index} className="py-1 pl-2 border-b border-c4 flex cursor-pointer group" onClick={() => {handleRatingUpdate(index + 1)}}>
                                <div className="mr-2">
                                    rate
                                </div>
                                <div className="pl-1 text-c2 hover:text-c4 group-hover:text-c4">
                                    +
                                </div>
                                <div className="mx-auto">
                                    {index + 1}
                                </div>
                            </div>
                        ))}
                        </div>
                    )}
                </div>

                <div className="ml-4 mt-4 border-t border-c4 pr-40">
                    <div>
                        Description/Synposis:
                    </div>
                    <div className="mt-2 mb-4 pl-4">
                        {anime.description || "No description available"}
                    </div>
                </div>

                <div className="flex mt-4 mx-auto w-[90%]">
                    {animePrequel ? (
                    <div className={`border-t border-b border-c4 flex ${animeSequel ? 'w-[50%] border-r' : 'w-[100%] border-r-0'}`}>
                        {loadingPrequel ? (
                            <div className="w-[87px] h-[123px] mx-auto">Loading...</div>
                        ) : animePrequel && animePrequel.image ? (
                            <Link to={`/anime/${animePrequel.id}`}>
                                <img 
                                    src={animePrequel.image} 
                                    alt="Anime Prequel Image" 
                                    className="w-[87px] h-[123px] my-4 mx-4" 
                                />
                            </Link>
                            
                        ) : (
                            <Link to={`/anime/${animePrequel.id}`}>
                            <div className="w-[87px] h-[123px] my-4 mx-4 bg-c4 text-c6 flex items-center justify-center"><span className="text-5xl">?</span></div>
                            </Link>
                        )}
                        <div className="my-4">
                            <div>{animePrequel?.titleEnglish || animePrequel?.titleJpRoman || "No title"}</div>
                            <div className="ml-2">prequel</div>
                        </div>
                    </div>
                    ) : null}
                    {animeSequel ? (
                    <div className={`border-t border-b border-c4 flex ${animePrequel ? 'w-[50%]' : 'w-[100%]'}`}>
                        {loadingSequel ? (
                            <div className="w-[87px] h-[123px] mx-auto">Loading...</div>
                        ) : animeSequel && animeSequel.image ? (
                            <Link to={`/anime/${animeSequel.id}`}>
                                <img 
                                    src={animeSequel.image} 
                                    alt="Anime Sequel Image" 
                                    className="w-[87px] h-[123px] my-4 mx-4" 
                                />
                            </Link>
                        ) : (
                            <Link to={`/anime/${animeSequel.id}`}>
                            <div className="w-[87px] h-[123px] my-4 mx-4 bg-c4 text-c6 flex items-center justify-center"><span className="text-5xl">?</span></div>
                            </Link>
                        )}
                        <div className="my-4">
                            <div>{animeSequel?.titleEnglish || animeSequel?.titleJpRoman || "No title"}</div>
                            <div>sequel</div>
                        </div>
                    </div>
                    ) : null}
                </div>
            </div>


        </div>
        </>
    )
}

export default AnimeDetailItem;



// fix routing of null user and non admin user both fail to re-render the page one redirect