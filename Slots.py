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
stakesL = ["x002"]*11 + ["x005"]*7 + ["x010"]*3 + ["x100"]*2 + ["****"]*2
stakesM = ["x002"]*9 + ["x005"]*6 + ["x010"]*4 + ["x050"]*3 + ["x100"]*2 + ["x250"]*1 + ["****"]*1
stakesH = ["x002"]*8 + ["x005"]*5 + ["x010"]*4 + ["x050"]*3 + ["x100"]*2 + ["x250"]*1 + ["x999"]*1 + ["****"]*1

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
        print("You do not have enough credits. Please enter a smaller amount.", "\n")
    elif inputCheat == 1:
        print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
    elif inputCheat == 2:
        print("1000 credits added to your balance. Who needs savings anyway?", "\n")
    elif inputCheat == 3:
        print("You've already used this cheat code!", "\n")
    else:
        print("\n")

def balanceBet():
    print("Your current balance is ", balance, " credits. \n", sep = "")

# Define function to set/reset global game parameters
def parSet(initial = False):
    global gameStage; gameStage = 1
    global spinNum; spinNum = 0
    if initial == True:
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
        print("You have", balance, "credits remaining in your account.")
        inputError = 0
        inputCheat = 0
        betType = input("Please enter low, medium, or high: ")
        if betType == "b":
            gameStage = gameStage - 1
        elif betType in ["Low", "low", "L", "l"]:
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
        if int(betAmount) > balance:
            inputError = 2
        elif int(betAmount) > 0:
            gameStage = gameStage + 1
        else:
            inputError = 1
    
    # ----- Step 2: Spin Wheels -----------------------------------------------
    
    # Choose amount to bet
    while gameStage == 2:
        clear()
        print("-"*5, "STEP 2: Spin Wheels", "-"*89, "\n")

        gameMessage()
        balanceBet()

        if spinNum == 0:
            print("[    ] [    ] [    ]\n\n", "Spin in progress...", sep = "")
            time.sleep(1.5)
        if spinNum == 1:
            w1 = spin(betType)
            print("[", *w1, "] [    ] [    ]\n\n", "Spin in progress.", sep = "")
            time.sleep(1.5)
        if spinNum == 2:
            w2 = spin(betType)
            print("[", *w1, "] [", *w2, "] [    ]\n\n", "Spin in progress.", sep = "")
            time.sleep(1.5)
        if spinNum == 3:
            w3 = spin(betType)
            print("[", *w1, "] [", *w2, "] [", *w3, "]\n\n", "Spin in progress.", sep = "")
            time.sleep(1.5)
        if spinNum == 4:
            print("[", *w1, "] [", *w2, "] [", *w3, "]\n", sep = "")
            input("Spin complete. Hit enter to continue... ")
            gameStage = gameStage + 1
        spinNum = spinNum + 1
        
    # ----- Step 3: Calculate Winnings ---------------------------------------  
     
    # test
    while gameStage == 3:
        clear()
        print("-"*5, "STEP 3: Calculate Winnings", "-"*82, "\n")
        
        gameMessage()
        
        if inputError != 1:
            if w1 == w2 == w3 != ["****"]:
                w = int(w1[0].replace('x', ''))
            elif (w1+w2+w3).count("****") == 1:
                tempW = w1+w2+w3
                tempW.remove("****")
                if(tempW[0] == tempW[1]):
                    w = int(tempW[0].replace('x', ''))
            elif (w1+w2+w3).count("****") == 2:
                tempW = w1+w2+w3
                tempW.remove("****")
                tempW.remove("****")
                w = int(tempW[0].replace('x', ''))
            elif (w1+w2+w3).count("****") == 3:
                w = 100
            else:
                w = -1
            winnings = w*betAmount
            balance = balance + winnings
            
        balanceBet()
        print("[", *w1, "] [", *w2, "] [", *w3, "]\n", sep = "")
        if w > 0:
            print("You matched a", "x"+str(w), "payout and won", winnings, "credits!")
        elif w < 0:
            print("You didn't match anything and lost", -winnings, "credits.")
        endGame = input("Enter \"m\" to return to wheel menu, or hit enter to play again: ")
        inputError = 0
        
        if endGame == "m":
            parSet()
        elif endGame == "":
            gameStage = 2
            spinNum = 0
        else:
            inputError = 1
            
        
        
        
        
    
    