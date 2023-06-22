import pandas as pd
import numpy as np
import datetime
# TAX CALCULATOR

def loadTaxTable(year):
    df = pd.read_excel("./taxTables/"+str(year)+".xlsx")
    return df

def getUserParameters():
    userParams = {}

    currentDate = datetime.date.today()
    currentYear = int(currentDate.strftime("%Y"))
    while True:
        try:
            userParams['year'] = int(input('Please type your tax year (yyyy): '))
            if userParams['year'] >= 2019 and userParams['year'] <= currentYear:
                break          
            else:
                raise Exception
        except:
            print("Please choose a year after 2019")

    while True:
        try:
            userParams['income'] = int(input('Please insert your weekly income without the $ sign: '))
            break          
        except:
            print("That's not a valid option!")

    return userParams
    
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

def main():
    userParams = getUserParameters()
    dfTaxTable = loadTaxTable(userParams['year'])
    taxPayable = calculateTax(dfTaxTable, userParams['income'])
    print("Your tax payble is: ${:,.2f}".format(np.rint(taxPayable)))


if __name__ == '__main__':
    main()
    