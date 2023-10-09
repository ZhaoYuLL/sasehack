// import Webcam from "react-webcam";
import { Link } from "react-router-dom";
import axios from 'axios';
import { useState } from "react";

function Generate() {

  const [emotion, setEmotion] = useState("");

  const getEmotion = async () => {
    try {
      const response = await axios.get("/analyze_emotion");
  
      // Handle the response data as needed
      console.log(response.data);

      const emotions = response.data["emotion"];
      const maxEmotion = Math.max(emotions["happy"], emotions["sad"], emotions["angry"]);

      switch (maxEmotion) {
        case emotions["happy"]:
          setEmotion("Happy");
          break;
        case emotions["sad"]:
          setEmotion("Sad");
          break;
        case emotions["angry"]:
          setEmotion("Angry");
          break;
        default:
          setEmotion("");
          break;
      }
    } catch (error) {
      // Handle any errors that occur during the request
      console.error('Error:', error);
    }
  };

  return (
    <>
    
      <div className="w-screen h-screen bg-navy-500">
        <div className="flex flex-col justify-center items-center w-full h-full">
            <div className='w-full h-1/6'/>
            <div className="flex flex-row justify-center items-center w-full h-2/3 bg-black">
                <div className="w-2/3 h-full">
                  <img src="{{ url_for('video') }}" width="50%" />
                </div>
                <div className="flex flex-col justify-center items-center w-1/3 h-full gap-12">
                    <div className="flex flex-col justify-center items-center gap-2">
                        <h1 className='lg:text-7xl text-5xl text-white font-bold uppercase transition duration-300 hover:drop-shadow-lg'>Emotion:</h1>
                        <p className='lg:text-5xl text-3xl text-white font-bold transition duration-300 hover:drop-shadow-lg'>{emotion}</p>
                    </div>

                    <Link to="/generate">
                        <button className="bg-navy-300 px-32 py-5 uppercase rounded-full drop-shadow-lg">
                            <h1 className='lg:text-3xl text-xl text-white font-bold uppercase transition duration-300 hover:drop-shadow-lg'>Create Playlist</h1>
                        </button>
                    </Link>
                </div>
            </div>
            <div className='w-full h-1/6'/>
        </div>
      </div>
    
    </>
  );
}

export default Generate;