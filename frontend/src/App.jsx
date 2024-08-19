import { useState, useEffect, useContext } from 'react';
import { Routes, Route } from 'react-router-dom';

import { UserContext } from './UserProvider';
import { getUser } from './utilities/user-service';

import HomePage from './HomePage/HomePage';
import AuthPage from './AuthPage/AuthPage';
import LandingPage from './LandingPage/LandingPage';

function App() {
  const { user, setUser } = useContext(UserContext);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userData = await getUser();
        setUser(userData);
      } catch (error) {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [setUser]);

  if (loading) {
    return <main></main>;
  }

  return (
    <main>
      {user ? (
        // has user
        <>
        <Routes>
          <Route path='/' element={<HomePage />}></Route>

        </Routes>
        </>
      ) : (
        // user is null
        <>
          <Routes>
          <Route path='/auth' element={<AuthPage />}></Route>
          <Route path='/' element={<LandingPage />}></Route>
          
          </Routes>
        </>
      )}
    </main>
  );
}

export default App;