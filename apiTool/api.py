from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np

# TAX CALCULATOR

class Request(BaseModel):
    year: str
    income: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# These files are small and don't take much to read/keep in memory. 
# We could do a preprocess and hold them in memory for quicker access.
def loadTaxTable(year):
    df = pd.read_excel("taxTables/"+str(year)+".xlsx")
    return df
    
def calculateTax(dfTaxTable, income):
    thresholdLimits = dfTaxTable.iloc[(dfTaxTable['income']-income).abs().argsort()[:2]]

    # Funky code to determine the threshold to use, eg threshold of 120k and 50k, and income of 90k
    # the limits will return the 120k as closer to 90k but we still want to use the 50k for our calculations
    if thresholdLimits.iloc[0][0] > income:
        base = thresholdLimits.iloc[1][2]
        rate = thresholdLimits.iloc[1][1]
        threshold = thresholdLimits.iloc[1][0]
        return base + ((income - threshold) * rate)
    else:
        base = thresholdLimits.iloc[0][2]
        rate = thresholdLimits.iloc[0][1]
        threshold = thresholdLimits.iloc[0][0]
        return base + ((income - threshold) * rate)

def calculator(request):
    response = {}
    dfTaxTable = loadTaxTable(request.year)
    taxPayable = calculateTax(dfTaxTable, int(request.income))
    response["taxPayable"] = np.rint(taxPayable)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/taxcalculator")
async def predict_sentiment(request: Request):
    return JSONResponse(calculator(request))