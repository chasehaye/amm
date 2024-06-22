//path
//user-service
//user-api
//send-request
import * as userAPI from './user-api';

export async function signUp(userData) {
  const token = await userAPI.signUp(userData);
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

export async function getUser() {
  try {
    const userData = await userAPI.grabUser();
    return userData;
  } catch (error) {
    console.error('Error fetching user:', error);
    return null;
  }
}

export function logOut() {
  localStorage.removeItem('token');
}

export async function login(credentials) {
  const token = await userAPI.login(credentials);
  localStorage.setItem('token', token.jwt);
  return getUser();
}

export function checkToken() {
  return userAPI.checkToken()
    .then(dateStr => new Date(dateStr));
}