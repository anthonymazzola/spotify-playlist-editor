import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { TrackProvider } from "./Contexts/TrackContext";
import Navbar from "./Components/Navbar";
import Hamburger from "./Components/Hamburger";
import Login from "./Components/Login";
import Footer from "./Components/Footer";
import PlaylistComponent from "./Pages/PlaylistComponent";
import Analytics from "./Pages/Analytics";
import Recommendations from "./Pages/Recommendations";
import Specialization from "./Pages/Specialization";
import "./App.css";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [token, setToken] = useState("");

  useEffect(() => {
    const hash = window.location.hash;
    let token = window.localStorage.getItem("token");

    if (!token && hash) {
      token = hash
        .substring(1)
        .split("&")
        .find((elem) => elem.startsWith("access_token"))
        .split("=")[1];

      window.location.hash = "";
      window.localStorage.setItem("token", token);
    }
    setToken(token);
    setIsLoggedIn(!!token); // Set isLoggedIn to true if token exists
  }, [isLoggedIn]);

  const logout = () => {
    setToken("");
    setIsLoggedIn(false);
    window.localStorage.removeItem("token");
  };

  return (
    <Router>
      <TrackProvider>
        <div className="whole-body">
          <div className="top-content">
            <div className="App-header">
              <div className="header-content">
                <h1>Applify</h1>
              </div>
              {!token ? (
                <Login />
              ) : (
                <button type={"logout"} onClick={logout}>
                  Logout
                </button>
              )}
            </div>
            <div className="Navbar">
              <Navbar />
              <Hamburger />
            </div>
          </div>
          <div className="page-body">
            <Routes>
              <Route
                path="/"
                element={
                  isLoggedIn ? <PlaylistComponent token={token} /> : <Login />
                }
              />
              <Route path="/analytics" element={<Analytics token={token} />} />
              <Route
                path="/recommendations"
                element={<Recommendations token={token} />}
              />
              <Route
                path="/specialization"
                element={<Specialization token={token} />}
              />
            </Routes>
          </div>
          <div className="Footer">
            <Footer />
          </div>
        </div>
      </TrackProvider>
    </Router>
  );
};

export default App;
