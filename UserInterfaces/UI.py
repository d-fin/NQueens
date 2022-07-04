from Classes.EstimateAndCalculations import Estimate


def UI(nVals):
    while True:
        print(f'\nWould you like to enter N-values or load a file with N-values?')
        print(f'1. Enter input value.')
        print(f'2. Load values from file.')
        print(f'3. Make a state space tree.')
        print(f'4. Quit')
        try:    
            choice = int(input())
            if choice > 4 or choice < 1: raise Exception("\nNot a valid option.")
        except Exception as e: 
            print(e)
        else:
            defaultInputFile = 'nVals.txt'
            if choice == 1: 
                nVals = enterInputValues(nVals)           
                return nVals 
            elif choice == 2: 
                nVals = loadFromFile(defaultInputFile)
                return nVals
            elif choice == 3:
                try:
                    n = int(input("\nEnter an n value: \n"))
                except ValueError as e: 
                    print("\nEnter an integer")
                except Exception as e:
                    print("\nThere was an error")
                else:
                    sizeOfTree, estimate = Estimate(n)
                    print("\nTree size: {:,}".format(sizeOfTree))
                    print("Estimated nodes visited to find solution: {:,}".format(estimate))
            else:
                print("Goodbye :)") 
                quit()       

''' Retrieves data from file. Returns a list of values of n read from the file. '''
def loadFromFile(defaultInputFile):
    try:
        valid = True
        fileName = None 
        fileName = checkIfFileExists()
        if fileName == False: raise FileNotFoundError
    except FileNotFoundError as e:
        while True: 
            print("\nFile not found!")
            print(f'Would you like to use the default file ({defaultInputFile}) or retry your file input?')
            retry = input("Enter \"retry\" or press Enter to continue with default... \n")
            if retry == "":
                valid = False
                break
            else: 
                fileName = checkIfFileExists()
                if fileName == False:
                    pass 
                else:
                    valid = True
                    break
    except Exception as e:
        print("\nThere was an issue with loading in the file")
        valid = False 
    finally: 
        if valid == True: 
            print(f'\n{fileName} has been found. ')
            nVals = readDataFromFile(fileName)
        if valid == False: 
            nVals = readDataFromFile(defaultInputFile)
        return nVals

''' Function that gets # of tests user wants to do if bad input default = 5. '''
def enterInputValues(nVals):
    print("\n*WARNING* after about 10 the program will run slowly!")
    print("Enter values for n. Press ENTER after each integer. \nEnter 0 when completed.")
    while True: 
        try: 
            n = input()
            if n.isdigit() == False: raise ValueError("\nMust be an integer!")
            else:
                n = int(n) 
                if n <= 0: break 
                if n < 4 and n >= 0: raise Exception("\nCannot be less than 4!")
                if n >= 13: raise Exception(f'Dont be ridiculous {n} is way too large....')
        except ValueError as e: print(e)
        except Exception as e: print(e)
        else:
            nVals.append(n) 
    print(f'N-values Entered: {nVals}')
    return nVals

''' Reading data from file. I did not use any try except clauses because I check if file exists and is able to be opened 
        before coming to this function (error handling happens in checkIfFileExists()) '''
def readDataFromFile(fileName):
    with open(fileName, 'r')as file:
        lines = file.readlines()
        nVals = [int(line.rstrip()) for line in lines]
    
    print(f'N-Values in file: {nVals}')
    return nVals

''' Checks to see if the file exists before attempting to open it. Returns false if the file doesnt exist. '''
def checkIfFileExists():
    try:
        fileName = str(input("\nEnter your file name: Do not enter file extension (Default = nVals.txt).\n"))
        fileName = fileName + ".txt"
        file = open(fileName, 'r')
    except Exception as e: 
        return False 
    else:
        file.close()
    return fileName