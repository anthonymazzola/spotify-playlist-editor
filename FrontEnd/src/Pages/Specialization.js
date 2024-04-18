import React, { useState, useEffect } from "react";
import { useTrack } from "../Contexts/TrackContext";
import SpecializationMenu from "../Components/SpecializationMenu";
import "./style.css";

const Specialization = ({ token }) => {
  const { playlistData } = useTrack();
  const [playlistName, setPlaylistName] = useState("");
  const [newUrl, setNewUrl] = useState("");
  const [selectedMood, setSelectedMood] = useState("");
  const [submitClicked, setSubmitClicked] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitClicked(true);
  };

  const handleInputChange = (e) => {
    setPlaylistName(e.target.value);
  };

  const handleMoodSelected = (selectedMood) => {
    setSelectedMood(selectedMood);
  };

  const fetchSpecUrl = async (trackIDs) => {
    try {
      if (!token) {
        console.error("Token not available");
        return;
      }

      const response = await fetch(
        `https://flask-server-ukjqkf-ca.proudsky-ad736f5d.eastus2.azurecontainerapps.io/create_playlist?token=${token}&nameOfPlaylist=${playlistName}&mood=${selectedMood}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            track_ids: trackIDs,
            nameOfPlaylist: playlistName,
          }),
        }
      );
      const newurl = await response.text();
      setNewUrl(newurl);
    } catch (error) {
      console.error("Error fetching new url:", error);
    }
  };

  useEffect(() => {
    if (
      submitClicked &&
      playlistName &&
      selectedMood &&
      playlistData.length > 0
    ) {
      const trackIDs = playlistData.map((track) => track.track_id);
      fetchSpecUrl(trackIDs);
      setSubmitClicked(false); // Resetting submit flag
    }
  }, [submitClicked, playlistName, selectedMood, playlistData, token]);

  return (
    <div className="specialization-container">
      <div className="form-bar">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={playlistName}
            onChange={handleInputChange}
            placeholder="Enter Playlist Name:"
          />
          <button type="submit">Submit</button>
        </form>
      </div>
      <div className="spec-menu">
        <SpecializationMenu onMoodSelected={handleMoodSelected} />
      </div>
      {newUrl && (
        <div className="new-url">
          <h3>An "{selectedMood}" Playlist</h3>
          <p>New URL:</p>
          <a href={newUrl} target="_blank" rel="noopener noreferrer">
            {newUrl}
          </a>
        </div>
      )}
    </div>
  );
};

export default Specialization;
