import React, { ChangeEvent, useState } from 'react';
import './App.css';

const  years: string[] = ['2019','2020','2021','2022','2023','2024',];

function Calculator() {
    const [year, setYear] = useState(years[0]);
    const [income, setIncome] = useState(0);

    const handleYearChange = (event: ChangeEvent<{ value: string }>) => {
        setYear(event?.currentTarget?.value);
    }

    const handleIncomeChange = (event: ChangeEvent<HTMLInputElement>) => {
        setIncome(parseInt(event.target.value, 10));
    }
    

  return (
    <div className="App">
      <header className="App-header">
          <p>Tax Year</p>
        <select onChange={handleYearChange}>
            {years.map( (year, index) => 
                <option value={`${year}`}>{year}-{years[index+1]}</option>
            ) }
        </select>
        <p>Yearly Income</p>
        <input type='number' value={income} onChange={handleIncomeChange}></input>
        <button onClick={}>
          CALCULATE YOUR TAX NOW WOOOOOO
        </button>
      </header>
    </div>
  );
}



export default Calculator;
