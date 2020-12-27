# ----- Import packages -----------------------------------------------------------------------------------------------------

# Import packages
import pandas as pd
import numpy as np
import random

# Define function to clear text from console
import os
def clear(): os.system('cls') #on Windows System
clear()





# ----- Pre-run setup -------------------------------------------------------------------------------------------------------

# Create table of bet types, odds, and payouts
df = pd.DataFrame(data = np.array([["36:1",     "35:1",  35],
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
                  index = ["single", "split", "square", "street", "doublestreet", "trio", "basket",
                           "low", "high", "black", "red", "odd", "even", "dozen", "column", "snake"],
                  columns = ["odds", "payout", "multiplier"])

# Set initial values
balance = 1000
gameStage = 1
inputError = False
cheatMessage = 0
cheatL = False
cheatS = False





# ----- Run game ------------------------------------------------------------------------------------------------------------

# Start running the game
while gameStage >= 1:
    
    # ----- Step 1: Select Bet ------------------------------------------------
    
    # Initial screen and betting prompt
    while gameStage == 1:
        clear()
        print("-"*5, "STEP 1: Select Bet", "-"*90, "\n")
        if inputError == 1:
            print("No previous menu to return to.", "\n")
        elif inputError == 2:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("At any time in the betting process, enter \"b\" to go back to the previous menu.")
        print("While on this screen, enter \"q\" to quit.", "\n")
        print("Inner bets are less likely to win but have higher payouts, and include:")
        print("single, split, square, street, doublestreet, trio, and basket.", "\n")
        print("Outer bets are more likely to win but have lower payouts, and include:")
        print("low, high, black, red, odd, even, dozen, column, and snake.", "\n")
        inputError = False
        betType = input("Please enter a bet type from one of the lists above, exactly as it appears: ")
        if betType == "b":
            inputError = 1
        elif betType == "q":
            gameStage = 0
        elif betType not in df.index:
            inputError = 2
        else:
            gameStage = gameStage + 1
    
    # ----- Step 2: Select Numbers (Inner Bets) -------------------------------  
    
    # Inner bet: straight/single (one number)
    while gameStage == 2 and betType == "single":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Single/straight bets involve betting on only one number.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Please enter a number in between 0 and 36: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber not in list(map(str, range(0, 37, 1))):
            inputError = True
        else:
            gameStage = gameStage + 1
            
    # Inner bet: split (2 board-adjacent numbers)        
    while gameStage == 2 and betType == "split":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Split bets involve betting on any 2 numbers that are adjacent on the board.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Please enter a number in between 0 and 36: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber == "0":
            nextNumber = [1, 2, 3]
            gameStage = gameStage + 0.5
        elif betNumber in list(map(str, range(1, 35, 3))):
            if int(betNumber) == 1:
                nextNumber = [0, int(betNumber) + 1, int(betNumber) + 3]
            elif int(betNumber) == 34:
                nextNumber = [int(betNumber) - 3, int(betNumber) + 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) + 1, int(betNumber) + 3]
            gameStage = gameStage + 0.5
        elif betNumber in list(map(str, range(2, 36, 3))):
            if int(betNumber) == 2:
                nextNumber = [0, int(betNumber) - 1, int(betNumber) + 1, int(betNumber) + 3]
            elif int(betNumber) == 35:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 1, int(betNumber) + 3]
            gameStage = gameStage + 0.5
        elif betNumber in list(map(str, range(3, 37, 3))):
            if int(betNumber) == 3:
                nextNumber = [0, int(betNumber) - 1, int(betNumber) + 3]
            elif int(betNumber) == 36:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1]
            else:
                nextNumber = [int(betNumber) - 3, int(betNumber) - 1, int(betNumber) + 3]
            gameStage = gameStage + 0.5
        else:
            inputError = True        
    while gameStage == 2.5:
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
            gameStage = gameStage - 0.5
        elif betNumber2 in nextNumber:
            betNumber = [betNumber, betNumber2]
            gameStage = gameStage + 0.5
        else:
            inputError = True
    
    # Inner bet: corner/square (a square of four board-adjacent numbers)   
    while gameStage == 2 and betType == "square":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Square/corner bets consist of four numbers n, n+1, n+3, and n+4 that are adjacent on the board.")
        print("Choices include 34, 35, and any multiples of 3.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber not in list(map(str, range(1, 33, 3))) or betNumber not in list(map(str, range(2, 33, 3))):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, 
                                       int(betNumber) + 3, int(betNumber) + 4]))
            gameStage = gameStage + 1
    
    # Inner bet: street (a row of three board-adjacent numbers)  
    while gameStage == 2 and betType == "street":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Street bets involve 3 consecutive numbers that form a row on the board.")
        print("Streets can start with 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, and 34.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber not in list(map(str, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34])):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, int(betNumber) + 2]))
            gameStage = gameStage + 1
    
    # Inner bet: double street (two consecutive rows of three board-adjacent numbers)  
    while gameStage == 2 and betType == "doublestreet":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Double street bets involve 6 consecutive numbers that form two rows on the board.")
        print("Double streets can start with 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, and 31.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Please enter a starting number from the list above: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber not in list(map(str, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31])):
            inputError = True
        else:
            betNumber = list(map(str, [int(betNumber), int(betNumber) + 1, int(betNumber) + 2,
                                       int(betNumber) + 3, int(betNumber) + 4, int(betNumber) + 5]))
            gameStage = gameStage + 1
    
    # Inner bet: trio (numbers 0, 1, 2 or 0, 2, 3)   
    while gameStage == 2 and betType == "trio":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Trio bets involve a group of numbers containing 0 and either 1/2 or 2/3.")
        print("The first trio is 0, 1, and 2; the second trio is 0, 2, and 3.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("First or second trio: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, [0, 1, 2]))
            gameStage = gameStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, [0, 2, 3]))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Inner bet: basket (numbers 0, 1, 2, 3) 
    while gameStage == 2 and betType == "basket":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Basket bets involve a group of the first four numbers (0, 1, 2, and 3).")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(0, 4, 1)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # ----- Step 2: Select Numbers (Outer Bets) -------------------------------  
    
    # Outer bet: low (numbers 1-18)
    while gameStage == 2 and betType == "low":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Low bets involve betting on all numbers 1-18.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(1, 19, 1)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: high (numbers 19-36)  
    while gameStage == 2 and betType == "high":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("High bets involve betting on all numbers 19-36.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(19, 37, 1)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: black
    while gameStage == 2 and betType == "black":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Black bets involve betting on all black numbers on the board.")
        print("This includes even numbers from 1-10 and 19-28, and odd numbers from 11-18 and 29-36.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: red    
    while gameStage == 2 and betType == "red":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Red bets involve betting on all red numbers on the board.")
        print("This includes odd numbers from 1-10 and 19-28, and even numbers from 11-18 and 29-36.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: odd    
    while gameStage == 2 and betType == "odd":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Odd bets involve betting on all odd numbers on the board. This exculdes zero.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(1, 37, 2)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: even    
    while gameStage == 2 and betType == "even":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Even bets involve betting on all even numbers on the board. This exculdes zero.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, range(2, 37, 2)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: dozen    
    while gameStage == 2 and betType == "dozen":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Dozen bets involve numbers in one of the three dozens. This exculdes zero.")
        print("The first dozen contains numbers 1-12, the second numbers 13-24, and the third numbers 25-36.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("First, second, or third dozen: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, range(1, 13, 1)))
            gameStage = gameStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, range(13, 25, 1)))
            gameStage = gameStage + 1
        elif betNumber in ["Third", "third", "3rd", "3"]:
            betNumber = list(map(str, range(25, 37, 1)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: column       
    while gameStage == 2 and betType == "column":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Column bets involve betting on an entire column of numbers on the board. This exculdes zero.")
        print("The first column contains numbers 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, and 34.")
        print("The second column contains numbers 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, and 35.")
        print("The third column contains numbers 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, and 36.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("First, second, or third column: ")
        if betNumber == "b":
            gameStage = gameStage - 1
        elif betNumber in ["First", "first", "1st", "1"]:
            betNumber = list(map(str, range(1, 35, 3)))
            gameStage = gameStage + 1
        elif betNumber in ["Second", "second", "2nd", "2"]:
            betNumber = list(map(str, range(2, 36, 3)))
            gameStage = gameStage + 1
        elif betNumber in ["Third", "third", "3rd", "3"]:
            betNumber = list(map(str, range(3, 37, 3)))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # Outer bet: snake        
    while gameStage == 2 and betType == "snake":
        clear()
        print("-"*5, "STEP 2: Select Numbers", "-"*86, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Snake bets involve betting on a set of numbers that form a snake-like pattern on the board.")
        print("These numbers are 1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, and 34.")
        print("Odds", df.loc[betType]["odds"], "against winning; payout", df.loc[betType]["payout"], "if successful.", "\n")
        inputError = False
        betNumber = input("Proceed? Y/N: ")
        if betNumber in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betNumber in ["Y", "y", "Yes", "yes"]:
            betNumber = list(map(str, [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]))
            gameStage = gameStage + 1
        else:
            inputError = True
    
    # ----- Step 3: Select Wager ----------------------------------------------
    
    # Choose amount to bet
    while gameStage == 3:
        clear()
        print("-"*5, "STEP 3: Select Wager", "-"*88, "\n")
        if inputError == 1:
            print("You do not have enough credits. Please enter a smaller amount.", "\n")
        elif inputError == 2:
            print("Please enter a number greater than zero.", "\n")
        elif inputError == 3:
            print("Invalid input, try again.", "\n")
        elif cheatMessage == 1:
            print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
        elif cheatMessage == 2:
            print("1000 credits added to your balance. Who needs savings anyway?", "\n")
        elif cheatMessage == 3:
            print("You've already used this cheat code!", "\n")
        else:
            print("\n")
        print("You have", balance, "credits remaining in your account.")
        inputError = False
        cheatMessage = 0
        betAmount = input("Please enter a whole amount to wager: ")
        if betAmount == "b":
            gameStage = gameStage - 1
        elif betAmount in ["Loan", "loan"]:
            if cheatL == True:
                cheatMessage = 3
            else:
                balance = balance + 2000
                cheatMessage = 1
                cheatL = True
        elif betAmount in ["Savings Account", "Savings account", "savings account", "savings Account", 
                           "SavingsAccount", "Savingsaccount", "savingsaccount", "savingsAccount"]:
            if cheatS == True:
                cheatMessage = 3
            else:
                balance = balance + 1000
                cheatMessage = 2
                cheatS = True
        else:
            try:
                if int(betAmount) > balance:
                    inputError = 1
                elif int(betAmount) <= 0:
                    inputError = 2
                else:
                    gameStage = gameStage + 1
            except ValueError:
                inputError = 3

    # ----- Step 4: Confirm Bet -----------------------------------------------

    # Confirm bet
    while gameStage == 4:
        clear()
        print("-"*5, "STEP 4: Confirm Bet", "-"*89, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        print("Your winning number(s):", *betNumber)
        print("You are betting", betAmount, "credits.")
        print("Odds", df.loc[betType]["odds"], "with", df.loc[betType]["payout"], "payout of", 
              int(betAmount)*int(df.loc[betType]["multiplier"]), "credits if successful.", "\n")
        inputError = False
        betConfirm = input("Proceed? Y/N: ")
        if betConfirm in ["b", "N", "n", "No", "no"]:
            gameStage = gameStage - 1
        elif betConfirm in ["Y", "y", "Yes", "yes"]:
            gameStage = 5
        else:
            inputError = True
    
    # ----- Step 5: Run numbers -----------------------------------------------  
    
    # Bet outcomes and prompt to reuse bet
    while gameStage == 5:
        clear()
        print("-"*5, "STEP 5: Results", "-"*93, "\n")
        if inputError == 1:
            print("Insufficient funds to reuse previous bet. You might want to go home...", "\n")
            print("Winning number:", *winningNumber)
            print("Your winning number(s):", *betNumber)
            print(balanceText)
        elif inputError == 2:
            print("Invalid input, try again.", "\n")
            print("Winning number:", *winningNumber)
            print("Your winning number(s):", *betNumber)
            print(balanceText)
        else:
            print("\n")
            winningNumber = random.sample(list(map(str, range(0, 37, 1))), 1)
            print("Winning number:", *winningNumber)
            print("Your winning number(s):", *betNumber)
            if str(*winningNumber) in betNumber:
                winnings = int(betAmount)*int(df.loc[betType]["multiplier"])
                balance = balance + winnings
                balanceText = "You won " + str(winnings) + " credits. Your balance is now " + str(balance) + " credits."
                print(balanceText)
            else:
                balance = balance - int(betAmount)
                balanceText = "You lost " + str(betAmount) + " credits. Your balance is now " + str(balance) + " credits."
                print(balanceText)
        inputError = False
        print("")
        betReuse = input("Would you like use your previous bet again? Y/N: ")
        if betReuse in ["b", "N", "n", "No", "no"]:
            gameStage = 1
        elif betReuse in ["Y", "y", "Yes", "yes"]:
            if balance < int(betAmount):
                inputError = 1
            else:
                gameStage = 5
        else:
            inputError = 2
        
