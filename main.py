import pandas as pd

# TAX CALCULATOR




# we need the tax year

# taxable income
# 1st attempt to just have the table there

def loadTaxTable(taxType):
    #Tax Scale	Weekly Earnings Less Than	Component A Factor	Component B Factor
    df = pd.read_excel(r"taxTables/2023.xlsx", sheet_name="STSL Statement of Formula - CSV")
    grouped = df.groupby("Tax Scale")
    return grouped.get_group(taxType)



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
    
def main():
    userParams = getUserParameters()
    taxTable = loadTaxTable(userParams['taxType'])



if __name__ == '__main__':
    main()
    