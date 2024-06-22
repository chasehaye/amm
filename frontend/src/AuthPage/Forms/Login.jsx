import React, { useState } from 'react';
import * as userService from '../../utilities/user-service'

function Login() {
    const [credentials, setCredentials] = useState({
        email: '',
        password: ''
      });
    const [error, setError] = useState('');
    
    function handleChange(evt) {
    setCredentials({ ...credentials, [evt.target.name]: evt.target.value });
    setError('');
    }
    
    async function handleSubmit(evt) {
    // Prevent form from being submitted to the server
    evt.preventDefault();
    try {
        // The promise returned by the signUp service method 
        // will resolve to the user object included in the
        // payload of the JSON Web Token (JWT)
        const user = await userService.login(credentials);
        console.log(user)

        setUser(user);
    } catch {
        setError('Log In Failed');
    }
    }
    
      return (
        <>
        <h5>
            login
        </h5>
          <div >
            <form autoComplete="off" onSubmit={handleSubmit}>
              <div className='flex flex-col max-w-60 m-auto'>
                <label className='text-center'>Email</label>
                <input type="text" name="email" value={credentials.email} onChange={handleChange} required />
    
                <label className='text-center'>Password</label>
                <input type="password" name="password" value={credentials.password} onChange={handleChange} required />
    
                <div className="mx-auto pt-4">
                  <button className="bg-C3 text-white py-1 px-4 rounded text-sm hover:bg-C8 mt-2 h-10 font-bold">Login</button>
                </div>
              </div>
            </form>
          </div>
          <p className="error-message">&nbsp;{error}</p>
        </>
      );
};

export default Login