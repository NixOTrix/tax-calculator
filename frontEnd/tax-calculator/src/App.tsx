import React from 'react';
import './App.css';

  
const routeChange = () =>{ 
  let path = `newPath`; 
}

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Hi and welcome to a simple landing page <br/> for my tax calculator app
        </p>
        <button onClick={routeChange}>
          CALCULATE YOUR TAX NOW
        </button>
      </header>
    </div>
  );
}



export default App;
