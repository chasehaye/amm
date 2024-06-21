import sendRequest from "./send-request";
const BASE_URL = '/api/user/';

export function register(userData) {
    return sendRequest(BASE_URL, 'POST', userData);
  }

export function login(credentials) {
    return sendRequest(`${BASE_URL}/login`, 'POST', credentials);
}