import React from "react";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";

const DisplayGraphs = ({ imageUrls }) => {
  const decodeBase64Image = (base64Image) => {
    return `data:image/png;base64,${base64Image}`;
  };

  return (
    <div className="graph-container">
      <Carousel showThumbs={false} className="carousel">
        {imageUrls.map((url, index) => (
          <img
            key={index}
            src={decodeBase64Image(url)}
            alt={`Image ${index}`}
            className="carousel-image"
          />
        ))}
      </Carousel>
    </div>
  );
};

export default DisplayGraphs;
