import React, { useState, useContext, createContext } from 'react';

const TrackContext = createContext();

export const useTrack = () => {
  return useContext(TrackContext);
};

export const TrackProvider = ({ children }) => {
  const [playlistData, setPlaylistData] = useState([]);

  const updatePlaylistData = (data) => {
    setPlaylistData(data);
  };

  const contextValue = {
    playlistData,
    updatePlaylistData,
  };

  return (
    <TrackContext.Provider value={contextValue}>
      {children}
    </TrackContext.Provider>
  );
};
