import sendRequest from "./send-request";
const BASE_URL = '/api/anime';

export function index(){
    return sendRequest(`${BASE_URL}/index`, 'GET');
}