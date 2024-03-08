// Home.js
import React from 'react';
import '../home.css'

function Home() {
 // Function to handle button click
 const handleClick = () => {
    console.log('Button clicked!');
    performLogic();
 };

 // Function to perform some logic
 const performLogic = () => {
    console.log('Performing some logic...');
 };

 return (
    <div>
      <h1>Automated Personalised Mood Based Song Selector</h1>
      <button class="border-black no-shadow" id="button_21" onClick={handleClick}>DETECT MOOD</button>
    </div>
 );
}

export default Home;
