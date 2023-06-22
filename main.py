import pandas as pd
import datetime
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
    taxPayable = 0

    

    return taxPayable
#     # formula : y = a * income - b
#     a = dfTaxRow["Component A Factor"].values[0]
#     b = dfTaxRow["Component B Factor"].values[0]
#     return a*income - b

def main():
    userParams = getUserParameters()
    dfTaxTable = loadTaxTable(userParams['taxType'], userParams['income'], userParams['year'])
    taxPayable = calculateTax(dfTaxTable, userParams['income'])
    print("Your tax payble is: $" + taxPayable)


if __name__ == '__main__':
    main()
    