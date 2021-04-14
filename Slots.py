# ----- Import packages -----------------------------------------------------------------------------------------------------

# Import packages
import random
import os





# ----- Pre-run setup -------------------------------------------------------------------------------------------------------

# Define function to clear text from console; confirmed to work on Windows
def clear(): os.system('cls')
clear()

# Define possible outcomes on wheels: low, medium, and high stakes
stakesL = [2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 10, 10, 100, "*", "*"]
stakesM = [2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 10, 10, 50, 100, 250, "*"]
stakesH = [2, 2, 2, 2, 2, 5, 5, 5, 5, 10, 10, 50, 100, 250, 1000, "*"]

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
        print("Please enter a number greater than zero.", "\n")
    elif inputError == 3:
        print("You do not have enough credits. Please enter a smaller amount.", "\n")
    elif inputCheat == 1:
        print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
    elif inputCheat == 2:
        print("1000 credits added to your balance. Who needs savings anyway?", "\n")
    elif inputCheat == 3:
        print("You've already used this cheat code!", "\n")
    else:
        print("\n")

# Define function to set/reset global game parameters
def parSet(initial = False):
    global gameStage; gameStage = 1
    if initial == True:
        global cheatUsed; cheatUsed = ""
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
        betAmount = input("Please enter a whole amount to wager: ")
        if betAmount == "b":
            gameStage = gameStage - 1
        elif betAmount in ["Loan", "loan"]:
            if cheatUsed in ["", "s"]:
                balance = balance + 2000
                inputCheat = 1
                cheatUsed = cheatUsed + "l"
            else:
                inputCheat = 3
        elif betAmount in ["Savings Account", "Savings account", "savings account", "savings Account", 
                           "SavingsAccount", "Savingsaccount", "savingsaccount", "savingsAccount"]:
            if cheatUsed in ["", "l"]:
                balance = balance + 1000
                inputCheat = 2
                cheatUsed = cheatUsed + "s"
            else:
                inputCheat = 3
        else:
            try:
                if int(betAmount) > balance:
                    inputError = 3
                elif int(betAmount) <= 0:
                    inputError = 2
                else:
                    gameStage = gameStage + 1
            except ValueError:
                inputError = 1
    
    
    
    
    