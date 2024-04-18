export default function DeleteButton(){

    function test(){
        alert('Test Passed!')
    }
    
    return(
        <div className='DeleteTrack'>
            <button onClick={test}>
                Delete Track
            </button>

            <style jsx = "true">{`
            button{
                background-image: linear-gradient(to right,#D83A56,     #FF616D, #66DE93);
                text-weight: bold;
                font-size: 24px;
                border: 3px solid;
                height: 75px;
                width: fit-content;
                font-weight: bold;
                font-size: 2em;
            }
            button:hover{
                background-color: white;
                color: green;
            }
            .Analytics{
                padding-top: 1em;
                padding-right: 1em;
                padding-bottom: 1em;
                padding-left: 1em;
            }    
        `}</style>
        </div>
    )
}