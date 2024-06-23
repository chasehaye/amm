import { useState, useEffect, useContext } from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';

import { UserContext } from './UserProvider';
import { getUser } from './utilities/user-service';

import HomePage from './HomePage/HomePage';
import AuthPage from './AuthPage/AuthPage';
import ListPage from './ListPage/ListPage';

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
        <>
          <HomePage />
          <ListPage />
        </>
      ) : (
        <AuthPage />
      )}
    </main>
  );
}

export default App;