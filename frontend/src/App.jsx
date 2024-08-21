import { useState, useEffect, useContext } from 'react';
import { Routes, Route } from 'react-router-dom';

import { UserContext } from './UserProvider';
import { getUser, adminVerify } from './utilities/user-service';

import HomePage from './UserPages/HomePage/HomePage';
import AuthPage from './AuthPage/AuthPage';
import LandingPage from './AllPages/LandingPage/LandingPage';
import AdminHomePage from './AdminPages/AdminHome/AdminHome';
import AddAnimePage from './AdminPages/AddAnimePage/AddAnimePage';

function App() {
  const { user, setUser } = useContext(UserContext);
  const [loading, setLoading] = useState(true);
  const [admin, setAdmin] = useState(null);

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


    const fetchAdminStatus = async () => {
      try {
          const adminStatus = await adminVerify();
          setAdmin(adminStatus)
      } catch (err) {
          setAdmin(false)
      } 
  }


    fetchUser();
    fetchAdminStatus();
  }, [setUser]);

  if (loading) {
    return <main></main>;
  }

  return (
    <main>
      {user ? (
        <>
          {/* User routes */}
          <Routes>
            <Route path='/' element={<HomePage />}></Route>
            {admin && (
              <>
                {/* Admin routes */}
                <Route path='/admin/home' element={<AdminHomePage />} />
                <Route path='/admin/anime/add' element={<AddAnimePage />} />
              </>
            )}
          </Routes>
        </>
      ) : (
        <>
          {/* Null routes */}
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