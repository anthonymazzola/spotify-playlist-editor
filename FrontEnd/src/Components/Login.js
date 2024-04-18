import React from "react";

const Login = () => {
  //variables for authentication
  const CLIENT_ID = "fe5fee17f1e84f3ea27fdeb3e548e43f";
  const REDIRECT_URI = "https://cs3050-applify-project.web.app/";
  const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize";
  const RESPONSE_TYPE = "token";
  const SCOPE = "playlist-modify-public";

  return (
    <a
      href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}&scope=${SCOPE}`}
    >
      Login to Spotify
    </a>
  );
};

export default Login;
