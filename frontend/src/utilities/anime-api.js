import sendRequest from "./send-request";
const BASE_URL = '/api/anime';

export function index(){
    return sendRequest(`${BASE_URL}/index`, 'GET');
}

export function createNewAnime(animeData){
    return sendRequest(`${BASE_URL}/create`, 'POST', animeData);
}

export function getAnimeRequest(animeId){
    console.log(animeId + "request ID")
    return sendRequest(`${BASE_URL}/${animeId}`, 'GET');
}