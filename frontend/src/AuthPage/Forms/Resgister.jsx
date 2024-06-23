import React, { useState, useContext } from 'react';
import * as userService from '../../utilities/user-service'
import { UserContext } from '../../UserProvider';

function Register(){
  const { user, setUser } = useContext(UserContext);
  const [credentials, setCredentials] = useState({
    name: '',
    email: '',
    password: '',
  });
  const [error, setError] = useState('');

  function handleChange(evt) {
    setCredentials({ ...credentials, [evt.target.name]: evt.target.value });
    setError('');
  }

  async function handleSubmit(evt) {
    evt.preventDefault();
    try{
      // register and retrieve user to set globally
      let user = await userService.register(credentials);
      const { name, ...loginUserObj } = credentials
      user = await userService.login( loginUserObj );
      setUser(user);
    }catch{
      setError('Registration Failed');
    }
  }

  return(
    <>
      <h5>
        register
      </h5>
      <div>
        <form autoComplete="off" onSubmit={handleSubmit}>
          <div>
            <label >Username</label>
            <input type="text" name="name" value={credentials.name} onChange={handleChange} required />

            <label>Email</label>
            <input type="email" name="email" value={credentials.email} onChange={handleChange} required />

            <label>Password</label>
            <input type="password" name="password" value={credentials.password} onChange={handleChange} required />

            <div>
              <button>Sign Up</button>
            </div>
          </div>
        </form>
      </div>
      <p className="error-message">&nbsp;{error}</p>
    </>
  )
      

}

export default Register