import React, { useState } from 'react';
import * as userService from '../../utilities/user-service'

function Register(){

    const [credentials, setCredentials] = useState({
        name: '',
        email: '',
        password: '',
        confirm: '',
        error: ''
      });
    const [error, setError] = useState('');

    function handleChange(evt) {
        setCredentials({ ...credentials, [evt.target.name]: evt.target.value });
        setError('');
    }

    async function handleSubmit(evt) {
        evt.preventDefault();
        try {
          const user = await userService.signUp(credentials);
          setUser(user);
        } catch {
          setError('Log In Failed');
        }
    }

    return(
        <>
        <h5>
            register
        </h5>
        </>
    )
      

}

export default Register