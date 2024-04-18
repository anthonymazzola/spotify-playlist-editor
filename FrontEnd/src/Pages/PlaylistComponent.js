import React, { useState } from "react";
import { useTrack } from "../Contexts/TrackContext";
import { getTestData } from "../Components/GetData.js";
import "./style.css";

const PlaylistComponent = ({ token }) => {
  const { playlistData, updatePlaylistData } = useTrack();
  const [playlistUrl, setPlaylistUrl] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    fetchData();
  };

  const handleInputChange = (e) => {
    setPlaylistUrl(e.target.value);
  };

  const fetchData = async () => {
    try {
      const response = await getTestData("get_playlist", token, playlistUrl);
      const playlist = response.tracks;
      updatePlaylistData(playlist); // Update playlist data in context
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <div className="form-bar">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={playlistUrl}
            onChange={handleInputChange}
            placeholder="Enter Playlist URL:"
          />
          <button type="submit">Submit</button>
        </form>
      </div>
      <div className="card-container">
        {playlistData.map((track, index) => (
          <div key={index} className="card">
            <div className="image-container">
              <img src={track.track_image} alt={`Track ${index}`} />
            </div>
            <h3>{track.track_name}</h3>
            <p>Artist: {track.artist_name}</p>
            <p>Popularity: {track.track_popularity}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PlaylistComponent;
