import React from 'react';
import './App.css';
import { useNavigate } from 'react-router-dom';


function App() {
  const navigate = useNavigate();
  
  const routeChange = () =>{ 
    navigate("/Calculator"); 
  }
  
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
