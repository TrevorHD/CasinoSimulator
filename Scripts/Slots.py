# ----- Import packages -----------------------------------------------------------------------------------------------------

# Import packages
import random
import time
import os





# ----- Pre-run setup -------------------------------------------------------------------------------------------------------

# Define function to clear text from console; confirmed to work on Windows
def clear(): os.system('cls')
clear()

# Define possible outcomes on wheels: low, medium, and high stakes
stakesL = ["x002"]*46 + ["x005"]*27 + ["x010"]*13 + ["x050"]*7 + ["x100"]*3 + ["****"]*4
stakesM = ["x002"]*51 + ["x005"]*25 + ["x010"]*11 + ["x050"]*5 + ["x100"]*3 + ["x250"]*1 + ["****"]*4
stakesH = ["x002"]*51 + ["x005"]*23 + ["x010"]*11 + ["x050"]*5 + ["x100"]*3 + ["x250"]*2 + ["x500"]*1 + ["****"]*4

# Function to spin a wheel once
def spin(stakes):
    if stakes == "low":
        return(random.sample(stakesL, 1))
    elif stakes == "medium":
        return(random.sample(stakesM, 1))
    elif stakes == "high":
        return(random.sample(stakesH, 1))

# Define function to return a specific error/cheat message for using information in global environment
def gameMessage():
    if inputError == 1:
        print("Invalid input, try again.", "\n")
    elif inputError == 2:
        print("You do not have enough credits for this.", "\n")
    elif inputCheat == 1:
        print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
    elif inputCheat == 2:
        print("1000 credits added to your balance. Who needs savings anyway?", "\n")
    elif inputCheat == 3:
        print("You've already used this cheat code!", "\n")
    else:
        print("\n")

# Define function to pring current balance
def balanceBet():
    print("Your current balance is ", balance, " credits. \n", sep = "")

# Define function to get per-game expected value of n games
# Used to "calibrate" the wheels and make game more or less favourable to player
# Slightly negative values are recommended to maintain house advantage
# This may take a bit for large values of n; n = 10000000 is recommended
def calibrate(stakes, n):
    for i in range(1, n + 1):
        if stakes == "low":
            betAmount = 10
        elif stakes == "medium":
            betAmount = 25
        elif stakes == "high":
            betAmount = 50
        if i == 1:
            wildcard = False
            winningList = []
        w1 = spin(stakes)
        w2 = spin(stakes)
        w3 = spin(stakes)
        if w1 == w2 == w3 != ["****"]:
            w = int(w1[0].replace('x', ''))
        elif (w1+w2+w3).count("****") == 1:
            tempW = w1+w2+w3
            tempW.remove("****")
            if(tempW[0] == tempW[1]):
                w = int(tempW[0].replace('x', ''))
            else:
                w = -1
        elif (w1+w2+w3).count("****") == 2:
            tempW = w1+w2+w3
            tempW.remove("****")
            tempW.remove("****")
            w = int(tempW[0].replace('x', ''))
        elif (w1+w2+w3).count("****") == 3:
            w = 0
            wildcard = True
        else:
            w = -1
        winnings = w*betAmount
        if wildcard == True and w > 0:
            wildcard = False
            winnings = w*betAmount*100
        winningList.append(winnings)
    return(sum(winningList)/len(winningList))

# Define function to set/reset global game parameters
def parSet(initial = False):
    global gameStage; gameStage = 1
    global spinNum; spinNum = 0
    if initial == True:
        global wildcard; wildcard = False
        global cheatUsed; cheatUsed = ""
        global betType; betType = "none"
        global inputError; inputError = 0
        global inputCheat; inputCheat = 0
        global balance; balance = 1000
        global betAmount; betAmount = 0
        
# Set initial values
parSet(initial = True)





# ----- Run game ------------------------------------------------------------------------------------------------------------

# Start running the game
while gameStage >= 1:
    
    # ----- Step 1: Select Wager ----------------------------------------------
    
    # Choose amount to bet
    while gameStage == 1:
        clear()
        print("-"*5, "STEP 1: Select Wager", "-"*88, "\n")
    
        # Accept bet amount or cheat code
        gameMessage()
        print("Your current balance is", balance, "credits. The following stakes levels are available:\n")
        print("   - Low: 10 credits per play.\n", "   - Medium: 25 credits per play.\n",
              "   - High: 50 credits per play.\n", sep = "")
        inputError = 0
        inputCheat = 0
        betType = input("Please choose a low, medium, or high stakes level: ")
        if betType in ["Low", "low", "L", "l"]:
            betType = "low"
            betAmount = 10
        elif betType in ["Medium", "medium", "M", "m"]:
            betType = "medium"
            betAmount = 25
        elif betType in ["High", "high", "H", "h"]:
            betType = "high"
            betAmount = 50
        elif betType in ["Loan", "loan"]:
            if cheatUsed in ["", "s"]:
                balance = balance + 2000
                inputCheat = 1
                cheatUsed = cheatUsed + "l"
            else:
                inputCheat = 3
        elif betType in ["Savings Account", "Savings account", "savings account", "savings Account", 
                           "SavingsAccount", "Savingsaccount", "savingsaccount", "savingsAccount"]:
            if cheatUsed in ["", "l"]:
                balance = balance + 1000
                inputCheat = 2
                cheatUsed = cheatUsed + "s"
            else:
                inputCheat = 3
        else:
            inputError = 1
        if int(betAmount) > balance:
            inputError = 2
        elif int(betAmount) > 0:
            gameStage = gameStage + 1
        
    
    # ----- Step 2: Spin Wheels -----------------------------------------------
    
    # Spin the three slot wheels
    while gameStage == 2:
        clear()
        print("-"*5, "STEP 2: Spin Wheels", "-"*89, "\n")

        # Print balance and error (if applicable)
        gameMessage()
        balanceBet()
        
        # Spin wheels sequentially
        if spinNum == 0:
            print("[    ] [    ] [    ]\n\n", "Spin in progress...", sep = "")
            time.sleep(1.5)
        if spinNum == 1:
            w1 = spin(betType)
            print("[", *w1, "] [    ] [    ]\n\n", "Spin in progress...", sep = "")
            time.sleep(1.5)
        if spinNum == 2:
            w2 = spin(betType)
            print("[", *w1, "] [", *w2, "] [    ]\n\n", "Spin in progress...", sep = "")
            time.sleep(1.5)
        if spinNum == 3:
            w3 = spin(betType)
            print("[", *w1, "] [", *w2, "] [", *w3, "]\n\n", "Spin in progress...", sep = "")
            time.sleep(1.5)
        if spinNum == 4:
            print("[", *w1, "] [", *w2, "] [", *w3, "]\n", sep = "")
            input("Spin complete. Hit enter to continue... ")
            gameStage = gameStage + 1
        spinNum = spinNum + 1
        
    # ----- Step 3: Calculate Winnings ---------------------------------------  
    
    # Calculate winnings and print earnings statements
    while gameStage == 3:
        clear()
        print("-"*5, "STEP 3: Calculate Winnings", "-"*82, "\n")
        
        # Print error if applicable
        gameMessage()
        
        # Calculate earnings
        if inputError != 1:
            if w1 == w2 == w3 != ["****"]:
                w = int(w1[0].replace('x', ''))
            elif (w1+w2+w3).count("****") == 1:
                tempW = w1+w2+w3
                tempW.remove("****")
                if(tempW[0] == tempW[1]):
                    w = int(tempW[0].replace('x', ''))
                else:
                    w = -1
            elif (w1+w2+w3).count("****") == 2:
                tempW = w1+w2+w3
                tempW.remove("****")
                tempW.remove("****")
                w = int(tempW[0].replace('x', ''))
            elif (w1+w2+w3).count("****") == 3:
                w = 0
            else:
                w = -1
            winnings = w*betAmount
            if wildcard == True:
                winningsWC = w*betAmount*100
                balance = balance + winningsWC
            else:
                balance = balance + winnings
        
        # Print balance and earnings statements
        balanceBet()
        print("[", *w1, "] [", *w2, "] [", *w3, "]\n", sep = "")
        if w > 0:
            if (w1+w2+w3).count("****") == 0:
                print("You matched a", "x"+str(w), "payout and won", winnings, "credits!")
            elif (w1+w2+w3).count("****") == 1:
                print("You matched a", "x"+str(w), "payout with a wildcard and won", winnings, "credits!")
            elif (w1+w2+w3).count("****") == 2:
                print("You matched a", "x"+str(w), "payout with two wildcards and won", winnings, "credits!")
        elif w < 0:
            print("You didn't match anything and lost", -winnings, "credits.")
        if w == 0 or wildcard == True:
            if wildcard == False:
                wildcard = True
                print("You matched three wildcards and will have your next win multiplied x100!")
            elif wildcard == True:
                wildcard = False
                print("Your previous wildcard bonus multiplied your winnings x100 for a total of", winningsWC, "credits!")
        
        # Replay or go to main menu
        endGame = input("Enter \"m\" to return to main menu, or hit enter to play again: ")
        inputError = 0
        if endGame == "m":
            parSet()
        elif endGame == "":
            gameStage = 2
            spinNum = 0
        else:
            inputError = 1
            
        