import pandas as pd 
from time import sleep

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

''' UI for exporting that provides choices to export specific data, print data, export all data. '''
def ExportUI(data):    
    result = convertToDataframe(data)
    outputFileName = None 
    defaultOutputFileName = "Data.xlsx"
    while True:
        try: 
            choice = showMenu()
            if choice == False: return True
        except Exception as e: print(f'\n{e}\nPlease enter one of the available choices. ')
        else:
            try:
                while True:
                    if choice == None: 
                        choice = showMenu()
                        if choice == False: return True 

                    if choice == 1:
                        print(result)
                        if stayOnExportMenu() == True: pass 
                        else: return True

                    elif choice == 2:
                        outputFileName = getFileName(defaultOutputFileName)
                        if exportToExcel(result, outputFileName) == False: print("\nFailed to export to excel")
                        else: 
                            print(f'\nData has been exported to excel file: {outputFileName}!') 
                            if stayOnExportMenu() == True: pass 
                            else: return True 

                    elif choice == 3: 
                        outputFileName = getFileName(defaultOutputFileName)
                        print(result)
                        if exportToExcel(result, outputFileName) == False: print("\nFailed to export to excel")
                        else: print(f'\nData has been exported to excel file: {outputFileName}!') 
                        if stayOnExportMenu() == True: pass 
                        else: return True 

                    elif choice == 4:
                        if printCols(result) == True:
                            if stayOnExportMenu() == True: pass 
                            else: return True    

                    elif choice == 5: return True 
                    choice = None 
            except Exception as e: print(f'{e}\nThere was an issue exporting/printing the data')
               

''' Shows menu and returns choice '''
def showMenu():
    print(f'\n1. Print data to terminal.')
    print(f'2. Export to excel.')
    print(f'3. Print and Export. ')
    print(f'4. Choose data to print.')
    print(f'5. Return to main menu - Will not print or export.')
    print(f'6. Quit - Terminate Program Execution.')
    choice = int(input())
    if choice > 6 or choice < 1: raise Exception(f'\n{choice} is not an option!')
    if choice == 5: 
        return False 
    if choice == 6: 
            print("Goodbye :)")
            quit()
    return choice 

''' Gets the exporting files name '''
def getFileName(defaultOutputFileName):
    outputFileType = ".xlsx"
    try: 
        print(f'\nDefault file is: {defaultOutputFileName}')
        print(f'If you wish to use the default input "0"')
        print("WARNING: Any data already in default file will be erased!")
        outputFileName = str(input("Enter the file name you wish to output to: (do not include file extension)\n"))
        if outputFileName == '0':
            outputFileName = "Data"
        if not outputFileName:
            print(f'\nNot a valid file option - using default file option')
            outputFileName = "Data" 
    except Exception as e: print(e)
    else:
        return outputFileName + outputFileType

''' Converts array of dictionaries to pandas dataframe. '''
def convertToDataframe(data):
    try:
        allDataFrames = []
        for i in data:
            df = pd.DataFrame(i)
            allDataFrames.append(df)
        
        result = pd.concat(allDataFrames, axis = 0, join = 'inner')
    except Exception as e: print(f'\n{e}\nCannot convert data to df.')
    else: return result

''' exports dataframe to excel. '''
def exportToExcel(result, outputFileName):
    try:
        result.to_excel(outputFileName)
    except Exception as e: 
        print(e)
        return False 
    else:
        return True 

''' Allows the user to choose what columns in the dataframe to print to the terminal. '''
def printCols(df):
    while True: 
        print(f'\nChoose what columns to print: ')
        print("1. Permutations")
        print("2. Naive Time")
        print("3. Improved Time")
        print("4. Full Tree")
        print("5. Estimation")
        print("6. Naive Nodes Visited")
        print("7. Improved Nodes Visited")
        print("8. Number of Solutions")
        print("Enter 0 to quit.")
        options = []
        while True: 
            try:
                choices = int(input())
                if choices < 0 or choices > 9: raise ValueError("\nChoose one of the provided options. ")
                if choices == 0: break 
                
            except ValueError as e: print(e)
            except Exception as e: print("\nError")
            else: options.append(choices)
        
        columns = {11 : "N Val", 1: "Permutations", 2 : "Naive Time", 3 : "Improved Time", 4 : "Full Tree",
                    5 : "Estimation", 6 : "Naive Nodes Visited", 7 : "Improved Nodes Visited", 8 : "Num of Solutions",
                    10 : "Matrices"}

        data_dict = df.to_dict('list')
        new_df = {}
        new_df['N Val'] = data_dict['N Val']
        if len(options) > 0:
            for i in options:
                if i in columns:
                    col_name = columns[i]
                    new_df[col_name] = data_dict[col_name]
            result = pd.DataFrame(new_df)
            result = result.sort_values(by=['N Val'], ascending=True)
            result = result.drop_duplicates()
            print(result)
            print("\nData successfully printed!")

        return True 

''' Allows the user to choose more exporting/print options. '''
def stayOnExportMenu():
    print(f'\n1. Return to print/export menu.')
    print(f'2. Return to main menu.')
    while True:
        try:
            x = int(input())
            if x < 1 or x > 2: raise ValueError("\nChoose one of the provided options.")
        except ValueError as e: print(e)
        except Exception as e: print(e)
        else:
            if x == 1: 
                print(f'Returning to exporting/print menu.....')
                sleep(2)
                return True 
            elif x == 2:
                return False 
