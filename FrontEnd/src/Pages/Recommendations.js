import React, { useEffect, useState } from "react";
import { useTrack } from "../Contexts/TrackContext";
import "./style.css";

const Recommendations = ({ token }) => {
  const { playlistData } = useTrack();
  const [recommendedSongs, setRecommendedSongs] = useState([]);

  useEffect(() => {
    if (playlistData.length > 0) {
      const trackIDs = playlistData.map((track) => track.track_id);
      fetchRecommendations(trackIDs);
    }
  }, [playlistData, token]);

  const fetchRecommendations = async (trackIDs) => {
    try {
      const response = await fetch(
        `https://flask-server-ukjqkf-ca.proudsky-ad736f5d.eastus2.azurecontainerapps.io/create_recommnedations?token=${token}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            track_ids: trackIDs.slice(0, 3),
          }),
        }
      );
      const data = await response.json();
      setRecommendedSongs(data.tracks);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div className="whole-body">
      <div className="card-container">
        {recommendedSongs.map((track, index) => (
          <div key={index} className="card">
            <div className="image-container">
              <img src={track.track_image} alt={`Track ${index}`} />
            </div>
            <h3>{track.track_name}</h3>
            <p>Artist: {track.artist_name}</p>
            <p>Track ID: {track.track_id}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Recommendations;
