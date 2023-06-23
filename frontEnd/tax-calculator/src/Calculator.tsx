import React, { ChangeEvent, useState } from 'react';
import './App.css';
import axios from "axios";

axios.create({
  baseURL: "http://localhost:8080",
  headers: {
    "Content-type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
});


const  years: string[] = ['2019','2020','2021','2022','2023','2024',];

function Calculator() {
    const [year, setYear] = useState(years[0]);
    const [income, setIncome] = useState(0);
    const [tax, setTax] = useState<number>();

    const handleYearChange = (event: ChangeEvent<{ value: string }>) => {
        setYear(event?.currentTarget?.value);
    }

    const handleIncomeChange = (event: ChangeEvent<HTMLInputElement>) => {
        setIncome(parseInt(event.target.value, 10));
    }

    const handleClick = async ()=>{
        try{
        setTax(undefined)
        const response = await axios.post("http://localhost:8080/taxcalculator", {
            income,
            year 
          })
        setTax(response.data.taxPayable as number)
        } catch(e){console.error(e)}

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
        <button onClick={handleClick}>
          CALCULATE YOUR TAX NOW WOOOOOO
        </button>
        {tax && <p>YOUR TAX PAYABLE IS: ${tax.toFixed(2)}</p>}
      </header>
    </div>
  );
}



export default Calculator;
