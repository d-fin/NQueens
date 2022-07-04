from time import sleep
import timeit  
import numpy as np 

from Classes.ImprovedNQueens import *
from Classes.NaiveNQueens import * 
from UserInterfaces.UI import * 
from Classes.EstimateAndCalculations import *
from UserInterfaces.Export import * 

''' Main '''
def main():
    # Decide if you want to use UI or just run a test script
    x = howToTest()
    
    # test script
    if x == 1:
        inputFileName = "nVals.txt"
        outputFileName = "Data.xlsx"
        testAmount = 10 
        data = []

        nVals = readDataFromFile(inputFileName)
        data = runAlgs(nVals, testAmount, data)
        result = convertToDataframe(data)
        if exportToExcel(result, outputFileName) == True: print(f'\nSuccessfully exported to {outputFileName}!')
        else: print("\nThere was a problem exporting to excel, please try again.")
    # UI
    else:
        while True:
            nVals = []
            data = []
            try: nVals = UI(nVals)
            except Exception: print(f'\nThere was an error getting the n-values. ') 
            else:
                try:
                    try:
                        # retrieve number of tests 
                        testAmount = getInput()
                    except Exception as e: print("\nError getting test amount.")
                    else:  
                        # test algorithms and return all of the data
                        input("\nPress Enter to start tests.....")
                        data = runAlgs(nVals, testAmount, data)
                except Exception as e: print(f'\n{e}\n\nThere was an error running your program')
                else:
                    # call to function that exports/displays data 
                    if ExportUI(data) == True: 
                        print(f'Returning to main menu.....')
                        sleep(2)

def runAlgs(nVals, testAmount, data):
    for n in nVals:
        dataForNVal = []
        for i in range(testAmount):
            sTotal = timeit.default_timer()
            # temp dictionary to store data for each test
            temp = {}
            # permutations and full size of state space tree along with estimated nodes visited
            perms = Perms(n)
            fullSizeOfTree, estimate = Estimate(n)

            # naive n queens algorithm 
            s1 = timeit.default_timer()
            ansNaive, naiveNodesVisited = NaiveNQueens(n)
            newNaiveNodesVisited = (naiveNodesVisited)
            r1 = timeit.default_timer() - s1 

            # improved n queens algorithm 
            s2 = timeit.default_timer()
            ansImproved, improvedNodesVisited = NQueens(n)
            newImprovedNodesVisited = improvedNodesVisited
            r2 = timeit.default_timer() - s2 

            if i == 0:
                sols = []
                for ans in ansImproved:
                    a = np.array(ans)
                    sols.append(a)                             
                sols = np.array(sols)

            #storing data 
            temp['N Val'] = n
            temp['Test Num'] = i + 1
            temp['Permutations'] = perms
            temp['Naive Time'] = r1 
            temp['Improved Time'] = r2 
            temp['Full Tree'] = fullSizeOfTree
            temp['Estimation'] = estimate 
            temp['Naive Nodes Visited'] = newNaiveNodesVisited
            temp['Improved Nodes Visited'] = newImprovedNodesVisited
            temp['Num of Solutions'] = len(ansImproved)
            #temp['Matrices'] = sols
            dataForNVal.append(temp)
                            
            # outputting test # per n, along with current time 
            # used to show the program is still running and how long it takes to do a test 
            # depending on n size 
            print(f'\nSuccess for value n = {n} for test number: {i + 1}')
            rTotal = timeit.default_timer() - sTotal
            print(f'Time taken for test #{i + 1} = {rTotal:.8f} seconds')
                            
        data.append(dataForNVal)
    return data

def howToTest():
    print("How would you like to run the program?")
    print("1. Test only option - no UI and default file \"nVals.txt\" will be used terminating the program after.")
    print("2. UI")
    while True: 
        try: 
            x = int(input())
            if x < 1 and x > 2: raise ValueError("Enter one of the provided options")
        except ValueError as e: print(e)
        except Exception as e: print("There was an error :(")
        else:
            return x 

def getInput():
    print(f'\nTest should be less than 20! :)')
    print("How many tests would you like to run per n-value? Or press Enter for default (tests = 5)...")
    while True:
        try: 
            x = input()
            if x == '': testAmount = 5
            else: 
                if x.isdigit == False: raise ValueError("\nNot an integer!")
                else: 
                    testAmount = int(x)
                    if testAmount >= 20 or testAmount < 1:
                        print(f'Invalid input using default value (tests = 5)')
                        testAmount = 5
                        return testAmount
        except ValueError as e: print(e)
        except Exception as e: print("\nThere was an error getting the value for number of test. ")
        else:
            return testAmount

if __name__ == '__main__':
    main()