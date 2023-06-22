import pandas as pd

# TAX CALCULATOR




# we need the tax year

# taxable income
# 1st attempt to just have the table there

def loadTaxTable(taxType, income, year):
    #Tax Scale	Weekly Earnings Less Than	Component A Factor	Component B Factor
    df = pd.read_excel("taxTables/"+year+".xlsx", sheet_name="STSL Statement of Formula - CSV")
    grouped = df.groupby("Tax Scale")
    dfTaxGroup = grouped.get_group(taxType)
    return dfTaxGroup.iloc[(dfTaxGroup['Weekly Earnings Less Than']-income).abs().argsort()[:1]]


def getUserParameters():
    userParams = {}

    while True:
        print("Please insert your tax type: \n (1) non-taxfree-threshold \n (2) taxfree-threshold \n")
        try:
            userParams['taxType'] = int(input('Please insert a valid integer input between 1 and 6'))
            if userParams['taxType'] > 0 and userParams['taxType'] < 7:
                break
            else:
                raise Exception                
        except:
            print("That's not a valid option!")


    while True:
        try:
            userParams['income'] = int(input('Please insert your weekly income without the $ sign: '))
            break          
        except:
            print("That's not a valid option!")

    return userParams
    
def calculateTax(dfTaxRow, income):
    # formula : y = a * income - b
    a = dfTaxRow["Component A Factor"].values[0]
    b = dfTaxRow["Component B Factor"].values[0]
    return a*income - b

def main():
    userParams = getUserParameters()
    dfTaxRow = loadTaxTable(userParams['taxType'], userParams['income'], userParams['year'])
    taxPayable = calculateTax(dfTaxRow, userParams['income'])


if __name__ == '__main__':
    main()
    