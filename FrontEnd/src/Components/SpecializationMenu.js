export default function SpecializationMenu({ onMoodSelected }) {
  const handleClickMood = (mood) => {
    onMoodSelected(mood); // Passing the mood back
  };

  function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function (event) {
    if (!event.target.matches(".dropbtn")) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains("show")) {
          openDropdown.classList.remove("show");
        }
      }
    }
  };
  return (
    <div className="specButton">
      <button onClick={myFunction} className="dropbtn">
        Choose your playlist mood:
      </button>
      <div id="myDropdown" className="dropdown-content">
        <button onClick={() => handleClickMood("calm")}>Calm</button>
        <button onClick={() => handleClickMood("upbeat")}>Upbeat</button>
        <button onClick={() => handleClickMood("dancy")}>Dancy</button>
        <button onClick={() => handleClickMood("running")}>Running</button>
        <button onClick={() => handleClickMood("instrumental")}>
          Instrumental
        </button>
      </div>
      <style jsx="true">{`
        .dropbtn {
          background-image: linear-gradient(
            to right,
            #d83a56,
            #ff616d,
            #66de93
          );
          color: black;
          padding: 16px;
          border: 3px solid;
          font-size: 16px;
          font-weight: bold;
          cursor: pointer;
        }

        .dropbtn:hover {
          color: green;
        }

        .dropdown {
          position: relative;
          display: inline-block;
        }

        .dropdown-content {
          display: none;
          position: absolute;
          background-color: #f1f1f1;
          min-width: 160px;
          box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
          z-index: 1;
        }

        .dropdown-content button {
          color: black;
          padding: 12px 16px;
          text-decoration: none;
          display: block;
          border: none;
          min-width: 160px;
        }

        .dropdown-content button:hover {
          background-color: #ddd;
        }

        .show {
          display: block;
        }

        .specButton {
          padding-top: 1em;
          padding-right: 1em;
          padding-bottom: 1em;
          padding-left: 1em;
        }
      `}</style>
    </div>
  );
}
