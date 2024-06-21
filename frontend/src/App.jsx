import { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom';
import './App.css'

import HomePage from './HomePage/HomePage'
import AuthPage from './AuthPage/AuthPage';
import ListPage from './ListPage/ListPage';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <main>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
      <div>
        <AuthPage />
        pages:
        <HomePage />
        <ListPage />
      </div>
      </main>
    </>
  )
}

export default App
