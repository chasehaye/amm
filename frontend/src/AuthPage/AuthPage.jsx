import { useState } from "react"
import Login from "./Forms/Login"
import Register from "./Forms/Resgister"

function AuthPage() {

    const[showLogin, setShowLogin] = useState(true);

    const toggleForm = () => {
        setShowLogin(!showLogin);
    }

    return(
        <>
            <button onClick={toggleForm}>
                {showLogin ? <p>Login</p> : <p> SignUp</p>}
            </button>

            {showLogin ? 
            <Register />
            : 
            <Login />
            }
        </>
    )
}

export default AuthPage