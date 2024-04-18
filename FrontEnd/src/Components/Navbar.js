import Hamburger from "./Hamburger";
import { useState } from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  const [hamburgerOpen, setHamburgerOpen] = useState(false);

  const toggleHamburger = () => {
    setHamburgerOpen(!hamburgerOpen);
  };

  return (
    <div>
      <div className="navigation">
        <ul className="navLink">
          <li>
            <Link to="/" className="navLink">
              Home
            </Link>
          </li>
          <li>
            <Link to="/analytics" className="navLink">
              Analytics
            </Link>
          </li>
          <li>
            <Link to="/recommendations" className="navLink">
              Recommendations
            </Link>
          </li>
          <li>
            <Link to="/specialization" className="navLink">
              Specialization
            </Link>
          </li>
        </ul>
        <div className="hamburger" onClick={toggleHamburger}>
          <Hamburger isOpen={hamburgerOpen} />
        </div>
      </div>

      <style jsx="true">{`
        .navigation {
          width: 100%;
          height: 50px;
        }

        .navigation ul {
          display: flex;
          flex-wrap: wrap;
          float: right;
          margin: 0px;
          padding: 0px;
          overflow: hidden;
        }

        .navigation ul li {
          list-style-type: none;
          padding-right: 10px;
          color: white;
          margin: 10px 0;
        }

        .navLink {
          color: white;
          padding: 15px 20px;
          text-align: center;
        }

        .hamburger {
          display: none;
          z-index: 6;
        }

        @media (max-width: 767px) {
          .hamburger {
            display: fixed;
            padding-top: 10px;
            margin-left: 10px;
            z-index: 6;
          }

          .navigation ul {
            display: ${hamburgerOpen ? "inline" : "none"};
            background-color: black;
            height: 100vh;
            width: 50vw;
            margin-top: 50px;
            position: fixed;
          }
        }
      `}</style>
    </div>
  );
}
