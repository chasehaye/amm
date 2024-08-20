import * as userAPI from './user-api';

export async function register(userData) {
  // register a user
   const token = await userAPI.register(userData);
   localStorage.setItem('token', token.jwt);
  return getUser();
}

export async function getToken() {
  //grab token
  const token = localStorage.getItem('token');
  //validate token
  if (!token) return null;
  // pull token exp
  const payload = JSON.parse(atob(token.split('.')[1]));
  //validate exp
  if (payload.exp < Date.now() / 1000) {
    // iff not valid remove token
    localStorage.removeItem('token');
    return null;
  }
  // if is valid return
  return token;
}

export async function getUser() {
  // grab user from database
  try {
    const userData = await userAPI.grabUser();
    return userData;
  } catch (err) {
    console.error('Error fetching user:', err);
    return null;
  }
}

export async function logOut() {
  localStorage.removeItem('token');
}

export async function login(credentials) {
  // login and set token in local storage
  const token = await userAPI.login(credentials);
  localStorage.setItem('token', token.jwt);
  return getUser();
}

export async function adminVerify(){
  try {
    const adminStatus = await userAPI.adminVerify();
    return adminStatus;
  } catch (err) {
    console.error('Error fetching user:', err);
    return false;
  }
}