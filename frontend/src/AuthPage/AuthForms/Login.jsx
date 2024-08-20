import React, { useState, useContext } from 'react';
import * as userService from '../../utilities/user-service'
import { UserContext } from '../../UserProvider';
import { useNavigate } from 'react-router-dom';

function Login() {
  const { setUser } = useContext(UserContext);
  const [credentials, setCredentials] = useState({
      email: '',
      password: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();
    
  function handleChange(evt) {
    setCredentials({ ...credentials, [evt.target.name]: evt.target.value });
    setError('');
  }
    
  async function handleSubmit(evt) {
    evt.preventDefault();
    try{
      // validate retrieve user to set globally
      const user = await userService.login(credentials);
      setUser(user);
      navigate('/');
    }catch{
      setError('Log In Failed');
    }
  }
    
  return (
    <>
      <div className='bg-c2 mt-4 pt-2 w-80 mx-auto rounded-lg'>
        <form autoComplete="off" onSubmit={handleSubmit}>
          <div className='flex flex-col max-w-60 m-auto mt-4'>
            <label className='text-center text-white'>Email</label>
            <input className='rounded-sm mt-1 mb-2' type="text" placeholder="Email" name="email" value={credentials.email} onChange={handleChange} required />

            <label className='text-center text-white'>Password</label>
            <input  className='rounded-sm mt-1' type="password" placeholder="Password" name="password" value={credentials.password} onChange={handleChange} required />

            <div className="mx-auto pt-4">
              <button className="bg-c1 hover:bg-c3 text-white hover:text-black py-1 px-4 rounded text-sm hover:bg-C8 h-8 font-bold mb-4">Login</button>
            </div>
          </div>
        </form>
      </div>
      <p className="error-message">&nbsp;{error}</p>
    </>
  );
};

export default Login