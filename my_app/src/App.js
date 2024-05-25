import React from 'react';
import { useRef,useState,useEffect } from 'react';
import axios from 'axios';
import './App.css';
function App(){
  const [image, setImage] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
  const [error, setError] = useState(null);
  
/*
  useEffect(()=>{
    fetch("/predict").then(
      res=>res.json()
    ).then(
      data=>{
        setData(data)
        console.log(data)
      }
    );
  },[]);
  */
  const handleImage = async (e) => {
    const file = e.target.files[0];
    setImage(file);
    setError(null);
    //setProcessedImage=null;
  };
  const formdatasubmit=async(e)=>{
    e.preventDefault();
    if (!image) {
      setError('No file selected');
      return;
    }
    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setProcessedImage(response.data.processed_image);
      setError(null);
    } catch (err) {
      console.error('Error predicting image:', err);
      setError('An error occurred while predicting the image.');
    }
  };
  return(
    <div className="container">
    <form onSubmit={formdatasubmit}>
    <input type="file" onChange={handleImage} />
    <input type="submit" value="Submit" />
    </form>
    {error && <div style={{ color: 'red' }}>{error}</div>}
    {processedImage && (
      <div>
        <h2>Predicted Image</h2>
        <img src={`data:image/jpg;base64,${processedImage}`} alt="Predicted" />
      </div>
    )}
  </div>
  )
}

export default App;