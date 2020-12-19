# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:08:32 2020

@author: Trevor Drees
"""

import os
def clear(): os.system('cls') #on Windows System
clear()



balance = 1000
betStage = 1



while betStage >= 1:
    
    while betStage == 1:
        # Clear text
        print("At any time in the betting process, enter \"b\" to go back.")
        betType = input("Please enter a bet type: ")
        betStage = betStage + 1
        
    while betStage == 2 and betType == "single":
        # Clear text
        betNumber = input("Please enter a whole number, 0-36: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber not in list(map(str, range(0, 37, 1))):
            print("Invalid input, try again.")
        else:
            betStage = betStage + 1
            
    while betStage == 2 and betType == "split":
        # WORK IN PROGRESS
        betStage = betStage + 1
        
    while betStage == 2 and betType == "street":
        # WORK IN PROGRESS
        betStage = betStage + 1
        
    while betStage == 2 and betType == "square":
        # WORK IN PROGRESS
        betStage = betStage + 1
        
    while betStage == 2 and betType == "doublestreet":
        # WORK IN PROGRESS
        betStage = betStage + 1
        
    while betStage == 2 and betType == "trio":
        # Clear text
        betNumber = input("First (0-1-2) or second (0-2-3) trio: ")
        if betNumber == "b":
            betStage = betStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, [0, 1, 2]))
            betStage = betStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, [0, 2, 3]))
            betStage = betStage + 1
        else:
            print("Invalid input, try again.")
        
    if betStage == 2 and betType == "firstfour":
        betNumber = list(map(str, range(0, 4, 1)))
        betStage = betStage + 1
    
    if betStage == 2 and betType == "low":
        betNumber = list(map(str, range(1, 19, 1)))
        betStage = betStage + 1
        
    if betStage == 2 and betType == "high":
        betNumber = list(map(str, range(19, 37, 1)))
        betStage = betStage + 1
        
    if betStage == 2 and betType == "black":
        betNumber = list(map(str, [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]))
        betStage = betStage + 1
        
    if betStage == 2 and betType == "red":
        betNumber = list(map(str, [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]))
        betStage = betStage + 1
        
    if betStage == 2 and betType == "odd":
        betNumber = list(map(str, range(1, 37, 2)))
        betStage = betStage + 1
        
    if betStage == 2 and betType == "even":
        betNumber = list(map(str, range(2, 37, 2)))
        betStage = betStage + 1
        
    while betStage == 2 and betType == "dozen":
        # Clear text
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
            print("Invalid input, try again.")
            
    while betStage == 2 and betType == "column":
        # Clear text
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
            print("Invalid input, try again.")
            
    if betStage == 2 and betType == "snake":
        betNumber = list(map(str, [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]))
        betStage = betStage + 1
    
    while betStage == 3:
        # Clear text
        print("You have", balance, "credits remaining in your account.")
        betAmount = input("Please enter a whole amount to wager:")
        if betAmount == "b":
            betStage = betStage - 1
        else:
            try:
                if int(betAmount) > balance:
                    print("You do not have enough credits. Please enter a smaller amount.")
                elif int(betAmount) <= 0:
                    print("Please enter a number greater than zero.")
                else:
                    betStage = betStage + 1
            except ValueError:
                print("Invalid input, try again.")

    while betStage == 4:
        # Clear text
        print("Your winning number is", betNumber, ".")
        print("You are betting", betAmount, "credits.")
        print("Odds 36:1, payout of", int(betAmount)*35, "credits at 35:1 if successful.")
        betConfirm = input("Proceed? Y/N: ")
        if betConfirm in ["b", "N", "n", "No", "no"]:
            betStage = betStage - 1
        elif betConfirm in ["Y", "y", "Yes", "yes"]:
            betStage = 0
        else:
            print("Invalid input, try again.")
            
