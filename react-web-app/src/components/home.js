import React, { useState, useEffect, useRef } from 'react';
import '../home.css';

function Home() {
 const [trackId, setTrackId] = useState(null);
 const [details, setDetails] = useState({
    artist_name: "",
    last_mood_detected: "",
    predicted_mood: "",
    song_name: "",
 });
 const iframeRef = useRef(null);

 useEffect(() => {
    if (trackId) {
      updateSpotifyEmbed(trackId);
    }
 }, [trackId]);

 const handleClick = () => {
    console.log('Button clicked!');

    fetch('http://localhost:81')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setTrackId(data.track_id);
        setDetails({
          artist_name: data.artist_name,
          last_mood_detected: data.last_mood_detected,
          predicted_mood: data.predicted_mood,
          song_name: data.song_name,
        });
      })
      .catch(error => console.error('Error fetching data:', error));
 };

 const updateSpotifyEmbed = (newTrackId) => {
    const newSrc = `https://open.spotify.com/embed/track/${newTrackId}?utm_source=generator`;
    if (iframeRef.current) {
      iframeRef.current.src = newSrc;
    }
 };

 return (
    <div>
      <h1>Automated Personalised Mood Based Song Selector</h1>
      <button className="border-black no-shadow" id="button_21" onClick={handleClick}>DETECT MOOD</button>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px', marginTop: '20px' }}>
        <div><button class="custom-btn btn-11">Artist Name: {details.artist_name}</button></div>
        <div><button class="custom-btn btn-11">Mood Detected By Facial Expressions: {details.last_mood_detected}</button></div>
        <div><button class="custom-btn btn-11">Mood Detected By Current Weather: {details.predicted_mood}</button></div>
        <div><button class="custom-btn btn-11">Song Name: {details.song_name}</button></div>
      </div>
      <div style={{ borderRadius: '12px', width: '100%', height: '352px', position: 'relative', marginTop: '20px' }}>
        <iframe
          ref={iframeRef}
          title="Spotify Embed"
          style={{ top: 0, left: 0, width: '100%', height: '65%', position: 'absolute', border: 0 }}
          allowFullScreen
          allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
          loading="lazy"
        />
      </div>
    </div>
 );
}

export default Home;
