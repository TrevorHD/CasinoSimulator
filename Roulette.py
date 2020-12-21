# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:08:32 2020

@author: Trevor Drees
"""

import os
def clear(): os.system('cls') #on Windows System
clear()

import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.array([["36:1",     "35:1",  35],
                                 ["17.5:1",   "17:1",  17],
                                 ["8.25:1",   "8:1",   8 ],
                                 ["11.333:1", "11:1",  11],
                                 ["5.167:1",  "5:1",   5 ],
                                 ["11.333:1", "11:1",  11],
                                 ["8.25:1",   "8:1",   8 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["1.056:1",  "1:1",   1 ],
                                 ["2.083:1",  "2:1",   2 ],
                                 ["2.083:1",  "2:1",   2 ],
                                 ["2.083:1",  "2:1",   2 ]]),
                  index = ["single", "split", "square", "street", "doublestreet", "trio", "firstfour",
                           "low", "high", "black", "red", "odd", "even", "dozen", "column", "snake"],
                  columns = ["odds", "payout", "multiplier"])

balance = 1000
betStage = 1
inputError = False


while betStage >= 1:
    
    while betStage == 1:
        clear()
        print("-"*5, "STEP 1: Select Bet", "-"*90, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Enter \"r\" on this screen to reuse your previous bet.")
        print("At any time in the betting process, enter \"b\" to go back.")
        inputError = False
        betType = input("Please enter a bet type: ")
        if betType not in df.index:
            inputError = True
        else:
            betStage = betStage + 1
        
    # Inner bet: straight/single (one number)
    while betStage == 2 and betType == "single":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Straight/single bets involve only one number.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Please enter a whole number, 0-36: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber not in list(map(str, range(0, 37, 1))):
            inputError = True
        else:
            betStage = betStage + 1
            
    # Inner bet: split (2 board-adjacent numbers)        
    while betStage == 2 and betType == "split":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Splits (2 numbers) consist of any 2 numbers adjacent on the board.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Please enter a whole number, 0-36: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber == "0":
            nextNumber = [1, 2, 3]
            betStage = betStage + 0.5
        elif betNumber in list(map(str, range(1, 35, 3))):
            if int(betNumber) == 1:
                nextNumber = [0, int(betNumber) + 1, int(betNumber) + 3]
            elif int(betNumber) == 34:
                nextNumber = [int(betNumber) - 3, int(betNumber) + 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) + 1, int(betNumber) + 3]
            betStage = betStage + 0.5
        elif betNumber in list(map(str, range(2, 36, 3))):
            if int(betNumber) == 2:
                nextNumber = [0, int(betNumber) - 1, int(betNumber) + 1, int(betNumber) + 3]
            elif int(betNumber) == 35:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 1, int(betNumber) + 3]
            betStage = betStage + 0.5
        elif betNumber in list(map(str, range(3, 37, 3))):
            if int(betNumber) == 3:
                nextNumber = [0, int(betNumber) - 1, int(betNumber) + 3]
            elif int(betNumber) == 36:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 3]
            betStage = betStage + 0.5
        else:
            inputError = True
            
    while betStage == 2.5:
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Numbers adjacent to your selection are", *nextNumber)
        inputError = False
        betNumber2 = input("Please enter one of the numbers above: ")
        nextNumber = list(map(str, nextNumber))
        if betNumber2 == "b":
            betStage = betStage - 0.5
        elif betNumber2 in nextNumber:
            betNumber = [betNumber, betNumber2]
            betStage = betStage + 0.5
        else:
            inputError = True
    
    # Inner bet: corner/square (a square of four board-adjacent numbers)   
    while betStage == 2 and betType == "square":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Squares (4 numbers) consist of numbers n, n+1, n+3, and n+4.")
        print("Choices include 34, 35, and any multiples of 3.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber not in list(map(str, range(1, 33, 3))) or betNumber not in list(map(str, range(2, 33, 3))):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, 
                                       int(betNumber) + 3, int(betNumber) + 4]))
            betStage = betStage + 1
    
    # Inner bet: street (a row of three board-adjacent numbers)  
    while betStage == 2 and betType == "street":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Streets (3 consecutive numbers) start with 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber not in list(map(str, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34])):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, int(betNumber) + 2]))
            betStage = betStage + 1
    
    # Inner bet: double street (two consecutive rows of three board-adjacent numbers)  
    while betStage == 2 and betType == "doublestreet":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Double streets (6 consecutive numbers) start with 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber not in list(map(str, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31])):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, int(betNumber) + 2,
                                       int(betNumber) + 3, int(betNumber) + 4, int(betNumber) + 5]))
            betStage = betStage + 1
    
    # Inner bet: trio (numbers 0, 1, 2 or 0, 2, 3)   
    while betStage == 2 and betType == "trio":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Trios consist of numbers 0 and either 1/2 or 2/3.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("First (0, 1, 2) or second (0, 2, 3) trio: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, [0, 1, 2]))
            betStage = betStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, [0, 2, 3]))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Inner bet: first four (numbers 0, 1, 2, 3) 
    while betStage == 2 and betType == "firstfour":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("First four consists of numbers 0, 1, 2, and 3.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(0, 4, 1)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: low (numbers 1-18)
    while betStage == 2 and betType == "low":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Low bets consist of numbers 1-18.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(1, 19, 1)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: high (numbers 19-36)  
    while betStage == 2 and betType == "high":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("High bets consist of numbers 19-36.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(19, 37, 1)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: black
    while betStage == 2 and betType == "black":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Black bets consist of evens 1-10, odds 11-18, evens 19-28, and odds 29-36.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: red    
    while betStage == 2 and betType == "red":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Red bets consist of odds 1-10, evens 11-18, odds 19-28, and evens 29-36.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: odd    
    while betStage == 2 and betType == "odd":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Odd bets consist of all odd numbers between 1 and 36.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(1, 37, 2)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: even    
    while betStage == 2 and betType == "even":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Even bets consist of all even numbers between 1 and 36.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(2, 37, 2)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: dozen    
    while betStage == 2 and betType == "dozen":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Dozen bets consist of numbers 1-12, 13-24, or 25-36")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("First, second, or third dozen: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, range(1, 13, 1)))
            betStage = betStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, range(13, 25, 1)))
            betStage = betStage + 1
        elif betNumber in ["Third", "third", "3rd", "3"]:
            betNumber = list(map(str, range(25, 37, 1)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: column       
    while betStage == 2 and betType == "column":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Column bets consist of FILLER TEXT.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("First, second, or third column: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, range(1, 35, 3)))
            betStage = betStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, range(2, 36, 3)))
            betStage = betStage + 1
        elif betNumber in ["Third", "third", "3rd", "3"]:
            betNumber = list(map(str, range(3, 37, 3)))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Outer bet: snake        
    while betStage == 2 and betType == "snake":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Snake bets consist of numbers 1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, and 34.")
        print("Odds of", df.loc[betType]["odds"], "and payout of", df.loc[betType]["payout"], "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]))
            betStage = betStage + 1
        else:
            inputError = True
    
    # Choose amount to bet
    while betStage == 3:
        clear()
        print("-"*5, "STEP 3: Select Wager", "-"*88, "\n")
        if inputError == 1:
            print("You do not have enough credits. Please enter a smaller amount.", "\n")
        elif inputError == 2:
            print("Please enter a number greater than zero.", "\n")
        elif inputError == 3:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("You have", balance, "credits remaining in your account.")
        inputError = False
        betAmount = input("Please enter a whole amount to wager: ")
        if betAmount == "b":
            betStage = betStage - 1
        else:
            try:
                if int(betAmount) > balance:
                    inputError = 1
                elif int(betAmount) <= 0:
                    inputError = 2
                else:
                    betStage = betStage + 1
            except ValueError:
                inputError = 3

    # Confirm bet
    while betStage == 4:
        clear()
        print("-"*5, "STEP 4: Confirm Bet", "-"*89, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Your winning number(s):", *betNumber)
        print("You are betting", betAmount, "credits.")
        print("Odds", df.loc[betType]["odds"], "with", df.loc[betType]["payout"], "payout of", 
              int(betAmount)*int(df.loc[betType]["multiplier"]), "credits if successful.")
        inputError = False
        betConfirm = input("Proceed? Y/N: ")
        if betConfirm in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betConfirm in ["Y", "y", "Yes", "yes"]:
            betStage = 0
        else:
            inputError = True
            
