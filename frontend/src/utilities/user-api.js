import sendRequest from "./send-request";
const BASE_URL = '/api/user';

export function register(userData) {
  return sendRequest(`${BASE_URL}/register`, 'POST', userData);
}

export function login(credentials) {
  return sendRequest(`${BASE_URL}/login`, 'POST', credentials);
}

export function grabUser() {
  return sendRequest(`${BASE_URL}/user`, 'GET');
}

export function checkToken() {
  return sendRequest(`${BASE_URL}/user`);
}