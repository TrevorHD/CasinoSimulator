# ----- Import packages -----------------------------------------------------------------------------------------------------

# Import packages
import random
import os





# ----- Pre-run setup -------------------------------------------------------------------------------------------------------

# Create a double-deck of cards
deck = list(map(str, range(2, 11, 1)))*8 + ["J", "Q", "K", "A"]*8

# Define function to clear text from console; confirmed to work on Windows
def clear(): os.system('cls')
clear()

# Define function to shuffle double-deck
def shuffle():
    shuffleCards = random.sample(deck, len(deck))
    return shuffleCards

# Define function to check sum of any given hand
def handSum(hand):
    try:
        hSum = sum(list(map(int, hand)))
    except ValueError:
        if "A" in hand:
            h1 = ["10" if x == "J" or x == "Q" or x == "K" else x for x in hand]
            h1 = ["11" if x == "A" else x for x in h1]
            hSum = sum(list(map(int, h1)))
            while hSum > 21 and "11" in h1:
                h1[h1.index("11")] = "1"
                hSum = sum(list(map(int, h1)))
        else:
            hSum = sum(list(map(int, ["10" if x == "J" or x == "Q" or x == "K" else x for x in hand])))
    return hSum

# Define function to draw cards
def draw(types):
    if types == "player":
        cardPlayer.append(cardQueue.pop())
    if types == "dealer":
        cardDealer.append(cardQueue.pop())

# Define function to return a specific error/cheat message for using information in global environment
def gameMessage():
    if inputError == 1:
        print("Invalid input, try again.", "\n")
    elif inputError == 2:
        print("Please enter a number greater than zero.", "\n")
    elif inputError == 3:
        print("You do not have enough credits. Please enter a smaller amount.", "\n")
    elif inputError == 4:
        print("Insufficient funds to double bet!", "\n")
    elif inputError == 5:
        print("Insurance bet should be less than or equal to half of current bet, try again.", "\n")
    elif inputError == 6:
        print("Insufficient funds for desired insurance bet, try again.", "\n")
    elif inputCheat == 1:
        print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
    elif inputCheat == 2:
        print("1000 credits added to your balance. Who needs savings anyway?", "\n")
    elif inputCheat == 3:
        print("You've already used this cheat code!", "\n")
    else:
        print("\n")

# Define function to return win/loss message when neither player has blackjack
def endMessage(playerVerb, dealerVerb, scoreNoun, tie = False):
    if tie == True :
        print("Player and Dealer tie with ", handSum(cardPlayer), ".", sep = "")
        print("Push; bet refunded to player.")
    elif tie == False:
        print("Player ", playerVerb, " with ", handSum(cardPlayer),
              " and dealer ", dealerVerb, " with ", handSum(cardDealer), ".", sep = "")
        print(scoreNoun, "of", betAmount, "credits.")
    print("Your balance is now", balance, "credits.", "\n", "\n", "\n")

# Define function to state your outstanding balance and bet        
def balanceBet():
    try:
        if int(insuranceAmount) > 0 and inputError not in [1, 2, 5, 6]:
            print("Your balance is", balance, "credits, with a bet of", betAmount, "plus", insuranceAmount, "in insurance.", "\n")
        else:
            print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")
    except ValueError:
        print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")

# Set initial values
doubled = False
split = False
dbjConfirmed = False
dbjCheck = False
reloopD1 = False
reloopD2 = False
reloopD3 = False
inputError = 0
inputCheat = 0
balance = 1000
betAmount = 0
insuranceAmount = 0
gameStage = 1
dbjCheckStage = 1
dbjInsuranceStage = 0
decisionNumP = 1
decisionNumD = 1
cheatUsed = ""
turnEndTypeP = "none"
turnEndTypeD = "none"





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
                    gameStage = gameStage + 0.5
            except ValueError:
                inputError = 1
      
    # ----- Step 1.5: Initial dealing -----------------------------------------
    
    # Deal cards and prepare to check for blackjack
    while gameStage == 1.5:
        
        # Shuffle cards; deal to player and dealer
        cardQueue = shuffle()
        cardDealer = []
        cardPlayer = []          
        draw("dealer")
        draw("player")
        draw("dealer")
        draw("player")
        
        # Check for dealer blackjack
        if handSum(cardDealer) == 21:
            dbjConfirmed = True
        if cardDealer[1] in ["10", "J", "Q", "K", "A"]:
            dbjCheck = True
            if cardDealer[1] == "A":
                dbjInsuranceStage = 1
        gameStage = gameStage + 0.5
        
    # ----- Step 2: Player decisions ------------------------------------------
    
    # Allow player to take turn
    while gameStage == 2:
        clear()
        print("-"*5, "STEP 2: Player Turns", "-"*88, "\n")
        
        # Print initial messages and information
        gameMessage()
        print("Dealer totals ? with cards: ?", cardDealer[1])
        print("Player totals", handSum(cardPlayer), "with cards:", *cardPlayer)
        balanceBet()
        if decisionNumP == 1:
            print("You were given card(s)", *cardPlayer, "\n")
        elif turnEndTypeP != "stand" and turnEndTypeP != "surrender":
            print("You were given card(s)", cardPlayer[len(cardPlayer) - 1], "\n")
        else:
            print("\n")
        inputError = 0
        
        # Display insurance bet messages (if applicable)
        if dbjInsuranceStage == 1:
            decision = input("The dealer may possibly have blackjack. Place insurance bet? Y/N: ")
            if decision in ["N", "n", "No", "no"]:
                dbjCheckStage = 2.5
                insuranceAmount = 0
                dbjInsuranceStage = 0
            elif decision in ["Y", "y", "Yes", "yes"]:
                dbjInsuranceStage = 2
            else:
                inputError = 1
        elif dbjInsuranceStage == 2:
            insuranceAmount = input("Enter an amount less than or equal to half yout current bet: ")  
            dbjCheckStage = 1.5
            try:
                if int(insuranceAmount) > 0.5*int(betAmount):
                    inputError = 5
                elif int(insuranceAmount) <= 0:
                    inputError = 2
                elif int(insuranceAmount) > balance - int(betAmount):
                    inputError = 6
                else:
                    dbjInsuranceStage = 0
                    dbjCheckStage = 1.75
            except ValueError:
                inputError = 1
                    
        # Display dealer blackjack-checking messages before player turn
        if dbjCheck == True and dbjInsuranceStage == 0:
            if dbjCheckStage in [1, 2]:
                decision = input("The dealer checks the hole card for blackjack. Hit enter to continue... ")
                dbjCheckStage = 3
            elif dbjCheckStage in [2.5, 1.75]:
                dbjCheckStage = 2
            elif dbjCheckStage == 3:
                if int(insuranceAmount) == 0:
                    if dbjConfirmed == False:
                        decision = input("The dealer does not have blackjack. Hit enter to continue... ")
                        dbjCheckStage = 3.5
                    elif dbjConfirmed == True:
                        gameStage = gameStage + 1
                elif int(insuranceAmount) > 0:
                    if dbjConfirmed == False:
                        decision = input("The dealer does not have blackjack, and you lose your insurance bet. Hit enter to continue... ")
                        balance = balance - int(insuranceAmount)
                        insuranceAmount = 0
                        dbjCheckStage = 3.5
                    elif dbjConfirmed == True:
                        gameStage = gameStage + 1
            elif dbjCheckStage == 3.5:
                dbjCheckStage = 4
                dbjCheck = False
            
        # Check player hand for bust or blackjack
        if dbjCheck == False and dbjCheckStage not in [2, 3, 3.5]:
            if handSum(cardPlayer) > 21:
                if doubled == False:
                    turnEndTypeP = "bust"
                else:
                    turnEndTypeP = "doubleBust"
            elif handSum(cardPlayer) == 21 and decisionNumP == 1:
                turnEndTypeP = "blackjack"
            elif handSum(cardPlayer) <= 21 and doubled == True:
                turnEndTypeP = "doubleStand"
        
        # End-of-turn messages for player
        if dbjCheck == False and dbjCheckStage not in [2, 3, 3.5]:
            if turnEndTypeP == "blackjack":
                decision = input("You have blackjack. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeP == "bust":
                decision = input("You bust; now it is the dealer's turn. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeP == "doubleBust":
                decision = input("You double down and bust; now it is the dealer's turn. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeP == "stand":
                decision = input("You stand and your turn is over; now it is the dealer's turn. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeP == "doubleStand":
                decision = input("You double down and stand; now it is the dealer's turn. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeP == "surrender":
                decision = input("You surrender and your turn is over; now it is the dealer's turn. Hit enter to continue... ")
                betAmount = int(betAmount)*0.5
                gameStage = gameStage + 1
            else:
                # note: will put in option for split later
                if decisionNumP == 1:
                    decision = input("Your move. Hit, stand, double down, or surrender: ")
                elif decisionNumP > 1:
                    decision = input("You're still in. Hit or stand: ")
                if decision in ["Hit", "hit"]:
                    draw("player")
                    turnEndTypeP = "hit"
                elif decision in ["Stand", "stand"]:
                    turnEndTypeP = "stand"
                elif decision in ["Double Down", "Double down", "double down", "double Down",
                                  "Doubledown", "DoubleDown", "doubledown", "doubleDown"] and decisionNumP == 1:
                    if balance < int(betAmount)*2:
                        inputError = 4
                    else:
                        doubled = True
                        betAmount = int(betAmount)*2
                        draw("player")
                    turnEndTypeP = "doubleDown"
                elif decision in ["Surrender", "surrender"] and decisionNumP == 1:
                    turnEndTypeP = "surrender"
                else:
                    inputError = 1
                if inputError == 0:
                    decisionNumP = decisionNumP + 1
        
        # If checking for dealer blackjack, advance to next step of this process
        if dbjCheck == False and dbjCheckStage == 3:
            dbjCheckStage = dbjCheckStage + 1
            
    # ----- Step 3: Dealer decisions ------------------------------------------
    
    while gameStage == 3:
        clear()
        print("-"*5, "STEP 3: Dealer Turns", "-"*88, "\n", "\n", "\n")
        
        # Print initial messages and information
        print("Dealer totals", handSum(cardDealer), "with cards:", *cardDealer)
        print("Player totals", handSum(cardPlayer), "with cards:", *cardPlayer)
        balanceBet()
        if decisionNumD == 1:
            print("\n")
            decision = input("Dealer reveals hole card. Press enter to continue... ")
        elif turnEndTypeD == "blackjack":
            print("\n")
            decision = input("Dealer has blackjack. Hit enter to continue... ")
            gameStage = gameStage + 1
        elif decisionNumD > 1 and (turnEndTypeD == "hit" or turnEndTypeD == "hitStand" or turnEndTypeD == "hitStandFirst"):
            print("Dealer was given card(s)", cardDealer[len(cardDealer) - 1], "\n")
        else:
            print("\n")
        
        # Check dealer hand for bust or blackjack
        if handSum(cardDealer) == 21 and decisionNumD == 1:
            turnEndTypeD = "blackjack"
        if handSum(cardDealer) > 21:
            turnEndTypeD = "bust"
        elif handSum(cardDealer) <= 16:
            draw("dealer")
            turnEndTypeD = "hit"
        
        # Decide if dealer should hit or stand
        if handSum(cardDealer) in range(17, 22, 1) and turnEndTypeD != "blackjack":
            if decisionNumD == 1 and turnEndTypeD == "hit":
                turnEndTypeD = "hitStandFirst"
                reloopD1 = True
            elif decisionNumD > 1 and turnEndTypeD == "hit":
                turnEndTypeD = "hitStand" 
                reloopD1 = True
            elif (turnEndTypeD == "hitStand" or turnEndTypeD == "hitStandFirst") and reloopD1 == True:
                reloopD1 = False
                reloopD2 = True
            elif turnEndTypeD == "hitStand" and reloopD2 == True:
                reloopD3 = True
            elif decisionNumD > 1:
                turnEndTypeD = "stand"
        
        # End-of-turn messages for dealer
        if turnEndTypeD != "blackjack":    
            if turnEndTypeD == "bust":
                decision = input("Dealer hits and busts. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeD == "stand":
                decision = input("Dealer stands. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeD == "hitStandFirst" and reloopD2 == True:
                decision = input("Dealer hits and then stands. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif turnEndTypeD == "hitStand" and reloopD3 == True:
                decision = input("Dealer hits and then stands. Hit enter to continue... ")
                gameStage = gameStage + 1
            elif decisionNumD > 1 and turnEndTypeD != "hitStandFirst" and (turnEndTypeD != "hitStand" or (turnEndTypeD == "hitStand" and reloopD1 == True)):
                decision = input("Dealer hits. Press enter to continue... ")
        if inputError == 0:
            decisionNumD = decisionNumD + 1
        
    # ----- Step 4: Results ---------------------------------------------------
    
    # Print appropriate result message
    while gameStage == 4:
        clear()
        print("-"*5, "STEP 4: Results", "-"*93, "\n", "\n", "\n")
        
        # Messages for instances where the player or dealer has blackjack
        if turnEndTypeD == "blackjack" and turnEndTypeP != "blackjack":
            if int(insuranceAmount) > 0:
                print("Dealer has blackjack; player loses, but collects insurance.")
                print("Loss of ", betAmount, ", but ", insuranceAmount, " collected from insurance.", sep = "")
                balance = balance - int(betAmount) + int(insuranceAmount)
                print("Your balance is now", balance, "credits.", "\n", "\n", "\n")
            else:
                print("Dealer has blackjack; player loses.")
                print("Loss of ", betAmount, ".", sep = "")
                balance = balance - int(betAmount)
                print("Your balance is now", balance, "credits.", "\n", "\n", "\n")
        elif turnEndTypeD != "blackjack" and turnEndTypeP == "blackjack":
            print("Player has blackjack; dealer loses.")
            print("Payout of ", 0.5*int(betAmount), ".", sep = "")
            balance = balance + 0.5*int(betAmount)
            print("Your balance is now", balance, "credits.", "\n", "\n", "\n")
        elif turnEndTypeD == "blackjack" and turnEndTypeP == "blackjack":
            print("Player and Dealer both have blackjack.")
            print("Push; bet refunded to player.")
            print("Your balance is now", balance, "credits.", "\n", "\n", "\n")
        
        # Messages for instances where the player or dealer does not have blackjack
        if turnEndTypeD != "blackjack" and turnEndTypeP != "blackjack":
            if handSum(cardDealer) > 21 and handSum(cardPlayer) > 21:
                balance = balance - int(betAmount)
                endMessage("busts", "busts", "Loss")
            elif handSum(cardDealer) > 21 and handSum(cardPlayer) <= 21:
                balance = balance + int(betAmount)
                endMessage("wins", "busts", "Payout")
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) > 21:
                balance = balance - int(betAmount)
                endMessage("busts", "wins", "Loss")
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) > handSum(cardPlayer):
                balance = balance - int(betAmount)
                endMessage("loses", "wins", "Loss")
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) < handSum(cardPlayer):
                balance = balance + int(betAmount)
                endMessage("wins", "loses", "Payout")
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) == handSum(cardPlayer):
                endMessage("wins", "loses", "Payout", tie = True)
                
        # Continue and reset variables        
        input("Press enter to continue... ")
        turnEndTypeP = "none"
        turnEndTypeD = "none"
        doubled = False
        decisionNumP = 1
        decisionNumD = 1
        reloopD1 = False
        reloopD2 = False
        reloopD3 = False
        gameStage = 1
        dbjCheckStage = 1
        dbjCheck = False
        dbjInsuranceStage = 0
        dbjConfirmed = False
        
        
        
        
        
    # Rules: dealer must draw on 16 and stand on 17, blackjack pays 2:1, early surrender only, double down
    #        available on soft count (even with aces) on initial hand only, blackjack pays 3:2
    