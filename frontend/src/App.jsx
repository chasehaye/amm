import { useState, useEffect, useContext } from 'react'
import { Routes, Route } from 'react-router-dom';
import './App.css'

import HomePage from './HomePage/HomePage'
import AuthPage from './AuthPage/AuthPage';
import ListPage from './ListPage/ListPage';
import { UserContext } from './UserProvider';

function App() {
  const { user } = useContext(UserContext);

  return (
    <>
      <main>
        {user ? (
          <>
            <HomePage />
            <ListPage />
          </>
        ) : (
          <>
            <AuthPage />
          </>
        )}
      </main>
    </>
  )
}

export default App
