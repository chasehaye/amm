//path
//user-service
//users-api
//send-request
import * as usersAPI from './user-api';

export async function signUp(userData) {
  const token = await usersAPI.signUp(userData);
  //store token in local storage
  localStorage.setItem('token', token);
  return getUser();
}

export function getToken() {
  //validate token is not expired
  const token = localStorage.getItem('token');
  if (!token) return null;
  // experation check
  
  const payload = JSON.parse(atob(token.split('.')[1]));

  if (payload.exp < Date.now() / 1000) {
    localStorage.removeItem('token');
    return null;
   }
   return token;
}

export function getUser() {
  const token = getToken();
  return token ?
    JSON.parse(atob(token.split('.')[1])).user
    :
    null;
}

export function logOut() {
  localStorage.removeItem('token');
}

export async function login(credentials) {
  const token = await usersAPI.login(credentials);
  localStorage.setItem('token', token);
  return getUser();
}

export function checkToken() {
  return usersAPI.checkToken()
    .then(dateStr => new Date(dateStr));
}