// GlobalContext.js
import React, { createContext, useContext, useState } from 'react';

// Create a context object
const GlobalContext = createContext();

// Create a provider component
export const GlobalProvider = ({ children }) => {
  const [user, setUser] = useState({
    // Initialize your user variables here
    loggedInUser: null,
    authToken: null,
    // Add more user-related variables as needed
  });

  return (
    <GlobalContext.Provider value={{ user, setUser }}>
      {children}
    </GlobalContext.Provider>
  );
};

// Custom hook to use the global state
export const useUser = () => useContext(GlobalContext);