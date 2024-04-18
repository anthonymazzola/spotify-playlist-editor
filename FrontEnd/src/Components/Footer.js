export default function Footer(){
    return(
        <div>
            <footer>
                <div className="FooterText">
                    <h3> Hello! Welcome to our playlist website! </h3>
                        <p>We have multiple different services on this website:</p>
                        <ul>
                            <li>Enter the URL of the playlist you would like to look at after logging into Spotify.</li>
                            <li>Click on the moods tab to split your playlist into smaller playlists based on different moods and other factors.</li>
                            <li>Click on the analytics tab to look at graphs related to your playlist.</li>
                            <li>Click on the recommendations tab to see recommendations based on your music.</li>
                        </ul>
                </div>
            </footer>

            <style jsx = "true">{`
                footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-image: linear-gradient(to right, #D83A56, #FF616D, #66DE93);
                }
                .FooterText {
                    color: black;
                    text-align: center;
                    margin: auto 0;
                }

                .FooterText h3{
                    color: black;
                }

                .FooterText p{
                    color: black;
                }

            `}</style>

</div>

    
    )
}