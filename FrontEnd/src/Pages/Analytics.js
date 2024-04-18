import React, { useState, useEffect } from "react";
import { useTrack } from "../Contexts/TrackContext";
import DisplayGraphs from "../Components/DisplayGraphs";
import "./style.css";

const Analytics = ({ token }) => {
  const { playlistData } = useTrack();
  const [graphs, setGraphs] = useState([]);

  const fetchGraphs = async () => {
    const trackIDs = playlistData.map((track) => track.track_id);
    try {
      const response = await fetch(
        `https://flask-server-ukjqkf-ca.proudsky-ad736f5d.eastus2.azurecontainerapps.io/get_graphs?token=${token}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            track_ids: trackIDs,
          }),
        }
      );
      const encodedurl = await response.json();
      setGraphs(encodedurl);
      console.log(graphs);
    } catch (error) {
      console.error("Error fetching graphs:", error);
    }
  };

  useEffect(() => {
    if (playlistData.length > 0 && token) {
      fetchGraphs();
    }
  }, [playlistData, token]);

  return (
    <div className="analytics-body">
      <h3>Analytics Page</h3>
      <p>Please be patient while graphs are generating.</p>
      <DisplayGraphs imageUrls={graphs} />
    </div>
  );
};
export default Analytics;
